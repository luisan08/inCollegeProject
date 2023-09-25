from components.search import jobSearch, peopleSearch, skillSearch, jobPosting_attempts
from unittest import mock
from unittest.mock import patch
import pandas as pd
from io import StringIO
import pytest


#Tests the skill search function. 
@pytest.mark.parametrize("skillChoice",[1, 2, 3, 4, 5])
def test_skill_search(skillChoice, monkeypatch, capfd):
    monkeypatch.setattr('builtins.input', lambda _: skillChoice)
    skillSearch()
    out, _ = capfd.readouterr()
    assert "Under construction." in out

#Test of jobSearch function
mock_accounts_jobs_data = """Title,Description,Employer,Location,Salary,First,Last
Software Engineer,Develop software applications,ABC Inc.,New York,80000,John,Doe
"""
mock_accounts_jobs = pd.read_csv(StringIO(mock_accounts_jobs_data))

@patch('builtins.input', side_effect=['1', 'Software Engineer', 'Develop software applications', 'ABC Inc.', 'New York', '80000', '2'])
@patch('components.search.accounts_jobs', mock_accounts_jobs)
def test_jobSearch_post_job_success(mock_input, capfd):
    # Mock the 'input' function to provide user input
    jobSearch()
    out, _ = capfd.readouterr()
    
    assert "You have successfully posted a job!" in out


#Pytests for peopleSearch function
mock_accounts_data = """first,last
John,Doe
Alice,Smith
"""
mock_accounts = pd.read_csv(StringIO(mock_accounts_data))

#Tests if the first and last name entered by the user is not a part of InCollege system
@patch('builtins.input', side_effect=['1', 'Alice', 'Patel', '2'])
@patch('components.login.accounts', mock_accounts)
def test_peopleSearch_non_existing_user(mock_input, capfd):
    # Mock the 'input' function to provide user input
    peopleSearch()
    out, _ = capfd.readouterr()    
    assert "Username was not found." in out

#Tests if the user wants to return to people search  
@patch('builtins.input', side_effect=['3', '2'])
def test_peopleSearch_return_to_search(mock_input, capfd):
    # Mock the 'input' function to provide user input
    peopleSearch()
    out, _ = capfd.readouterr()   
    assert "Returning to People Search." in out

#Tests if the input of user is wrong
@patch('builtins.input', side_effect=['4', '2'])
def test_peopleSearch_invalid_option(mock_input, capfd):
    # Mock the 'input' function to provide user input
    peopleSearch()
    out, _ = capfd.readouterr()   
    assert "Invalid option. Returning to People Search." in out
