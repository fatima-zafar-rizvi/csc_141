
import requests
import unittest
from unittest.mock import patch, Mock

# Function to get Python repos
def get_python_repos():
    response = requests.get('https://api.github.com/search/repositories?q='
                            'language:python')
    return response

class TestPythonRepos(unittest.TestCase):
    
    @patch('requests.get')
    def test_get_python_repos(self, mock_get):
        # Mock the response from requests.get
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'items': [{'name': 'repo1'}, 
                                                     {'name': 'repo2'}]}
        mock_get.return_value = mock_response

        # Call the function you are testing
        response = get_python_repos()

        # Assertions
        self.assertEqual(response.status_code, 200)
        data = response.json()
        # Check that two repositories were returned
        self.assertEqual(len(data['items']), 2)
        # Check that at least one repository was returned
        self.assertGreater(len(data['items']), 0)
        # Check that more than one repository is returned
        self.assertGreater(len(data['items']), 1)

if __name__ == "__main__":
    unittest.main()



















'''
import pytest
import requests

# Function to get Python repos
def get_python_repos():
    response = requests.get('https://api.github.com/search/repositories?q='
    'language:python')
    return response

# Test suite for python_repos.py
def test_get_python_repos(mocker):
    # Mock the requests.get method
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'items': [{'name': 'repo1'}, 
    {'name': 'repo2'}]}
    mocker.patch('requests.get', return_value=mock_response)

    # Call the function you are testing
    response = get_python_repos()

    # Assertions
    assert response.status_code == 200  
    data = response.json()  
    # Check that two repositories were returned
    assert len(data['items']) == 2  
    # Check that at least one repository was returned
    assert len(data['items']) > 0  
    # Check that more than one repository is returned
    assert len(data['items']) > 1  

if __name__ == "__main__":
    pytest.main()
'''