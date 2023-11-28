#!/usr/bin/env python3

from flask import Flask, request
from flask import Flask, request, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Job Search</title>
        <link rel="stylesheet" href="{}">
    </head>
    <body>
        <h1>Welcome to the Job Search Portal</h1>
        <p>Please enter the type of job you are looking for:</p>
        <form action="/submit_job_type" method="POST">
            <input type="text" name="job_type" placeholder="Enter job type">
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    '''.format(url_for('static', filename='styles.css'))

@app.route("/submit_job_type", methods=["POST"])
def submit_job_type():
    user_input = request.form.get("job_type", "")
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Job Type Submitted</title>
        <link rel="stylesheet" href="{}">
    </head>
    <body>
        <h1>Job Type Submitted</h1>
        <p>You entered: {user_input}</p>
        <p>Thank you for submitting your job type. We'll assist you in finding relevant jobs.</p>
    </body>
    </html>
    '''.format(url_for('static', filename='styles.css'))

if __name__ == '__main__':
    app.run(debug=True)

