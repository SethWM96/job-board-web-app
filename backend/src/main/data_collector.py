#!/usr/bin/env python3

from pymongo import MongoClient
import requests
import json
from flask import Flask

app = Flask(__name__)

def fetch_job_data():    

    # Establish MongoDB connection
    MONGO_URI = 'mongodb://localhost:27017/jobdatabase'
    client = MongoClient(MONGO_URI)
    db = client.get_database()
    job_collection = db['job_data']

    adzuna_api = "https://api.adzuna.com/v1/api/jobs/us/search/1?app_id=8290d9dc&app_key=7cfb4897c4d351fa81a1d0a055be4fac&results_per_page=50"

    headers = {
        'Accept': 'application/json'
    }

    response = requests.get(adzuna_api, headers=headers)

    if response.status_code == 200:
        try:
            job_data = response.json().get('results', [])
            if job_data:  
                # Print or log the fetched job data
                print("Fetched Job Data:")
                print(json.dumps(job_data, indent=2))  # Print formatted JSON data

                # Check if job_data is not empty
                job_collection.insert_many(job_data)
                return 'Job data fetched and stored successfully!'
            else:
                return 'No job data found in the response.'
        except requests.exceptions.JSONDecodeError as e:
            return f"Error decoding JSON: {e}"
    else:
        return f"Failed to fetch data. Status code: {response.status_code}"

if __name__ == "__main__":
    fetch_job_data()