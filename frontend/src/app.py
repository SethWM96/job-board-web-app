#!/usr/bin/env python3

from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
MONGO_URI = 'mongodb://localhost:27017/jobdatabase'
client = MongoClient(MONGO_URI)
db = client.get_database()
job_data_collection = db['processed_job_data']

@app.route('/')
def index():
    quartile_options = ['Lower Quartile', 'Middle Quartile', 'Upper Quartile', 'Above Upper Quartile']
    return render_template('index.html', quartiles=quartile_options)

@app.route('/insights', methods=['GET'])
def insights():
    selected_quartile = request.args.get('quartile')  # Get the selected quartile from the query parameters

    # Retrieve specific job data based on the selected quartile
    job_results = job_data_collection.find({'Salary Quartile': selected_quartile}, {'title': 1, 'salary_max': 1, 'redirect_url': 1})
    job_list = list(job_results)

    return render_template('insights.html', jobs=job_list)

if __name__ == '__main__':
    app.run(debug=True)











