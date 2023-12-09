# Job Web Board App
## Overview
The Job Web Board App is a versatile application designed to fetch job data from the Adzuna API and store it efficiently in a MongoDB database. MongoDB, a NoSQL database tool, has been chosen to offer flexibility in integrating multiple APIs over time. The application incorporates a robust data analysis component that employs Pandas for data cleaning and salary analysis.

## Features
### Data Fetching: Utilizes the Adzuna API to fetch job data for storage.
### Data Analysis: Cleans and analyzes job data, segmenting salaries into quartiles for user insights.
### MongoDB Integration: Facilitates data storage and management using MongoDB's NoSQL capabilities.
### Flexibility: Designed to seamlessly integrate multiple APIs to expand the job data pool.
### User Interface: Provides an intuitive web interface where users can filter jobs by salary range preference.
Setup Instructions
##To set up and run the application locally, follow these steps:

Clone the repository.
Install project dependencies using pip install -r requirements.txt.
Set up the Flask app environment.
Run the Flask application.
Access the application at the specified localhost address.
Note: The current configuration may require local deployment due to MongoDB environment discrepancies. 

## Testing and Continuous Integration
The project incorporates a robust testing suite comprising unit tests and mock tests. Continuous Integration (CI) has been implemented to ensure code quality and reliability. While the CI build may fail due to MongoDB environment differences, local testing ensures seamless functionality.

Usage
Access the deployed application.
Choose the preferred salary range to explore job listings falling within that category.
Enjoy exploring comprehensive job insights based on salary quartiles!
Conclusion
The Job Web Board App offers a powerful platform for exploring job insights while utilizing cutting-edge technologies. For a seamless experience, consider deploying the application locally or through Heroku.
