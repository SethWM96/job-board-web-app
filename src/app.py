from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Job Search</title>
        <style>
            body {
                background-color: olive;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 0;
                padding: 20px;
            }
            form {
                display: inline-block;
                margin-top: 20px;
            }
            input[type="text"], input[type="submit"] {
                padding: 10px;
                margin: 5px;
                border: 2px solid white;
                border-radius: 5px;
                background-color: white;
                color: olive;
                font-family: Arial, sans-serif;
            }
            input[type="submit"]:hover {
                background-color: lightgray;
            }
        </style>
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
    '''

@app.route("/submit_job_type", methods=["POST"])
def submit_job_type():
    try:
        user_input = request.form.get("job_type", "")
        return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Job Type Submitted</title>
            <style>
                body {
                    background-color: olive;
                    color: white;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin: 0;
                    padding: 20px;
                }
                h1, p {
                    color: white;
                }
            </style>
        </head>
        <body>
            <h1>Job Type Submitted</h1>
            <p>You entered: {user_input}</p>
            <p>Thank you for submitting your job type. We'll assist you in finding relevant jobs.</p>
        </body>
        </html>
        '''
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

