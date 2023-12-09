import unittest
from unittest.mock import MagicMock, patch

import sys
sys.path.append('backend/src/main')
from data_collector import fetch_job_data

class TestFetchJobData(unittest.TestCase):

    @patch('requests.get')
    @patch('pymongo.MongoClient')
    def test_fetch_job_data_success(self, mock_mongo_client, mock_requests_get):
        # Mock the response from requests.get
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'results': [{'job_title': 'Software Engineer', 'company': 'Example Inc.'}]}

        mock_requests_get.return_value = mock_response

        # Mock the MongoDB collection insert_many method
        mock_collection = MagicMock()
        mock_db = MagicMock()
        mock_db.__getitem__.return_value = mock_collection
        mock_mongo_client.return_value.get_database.return_value = mock_db

        result = fetch_job_data()

        self.assertEqual(result, 'Job data fetched and stored successfully!')

    @patch('requests.get')
    def test_fetch_job_data_failure(self, mock_requests_get):
        # Mock the response from requests.get
        mock_response = MagicMock()
        mock_response.status_code = 500

        mock_requests_get.return_value = mock_response

        result = fetch_job_data()

        self.assertEqual(result, 'Failed to fetch data. Status code: 500')

if __name__ == '__main__':
    unittest.main()
