from unittest import mock
import pytest
import components.search
from components.search import jobSearch, peopleSearch, skillSearch, jobPosting_attempts
from unittest.mock import patch
import pandas as pd
from io import StringIO

@pytest.mark.parametrize("skillChoice",[1, 2, 3, 4, 5])
def test_skill_search(skillChoice, monkeypatch, capfd):
    monkeypatch.setattr('builtins.input', lambda _: skillChoice)
    skillSearch()
    out, _ = capfd.readouterr()
    assert "Under construction." in out

#Pytests for people function
mock_accounts_data = """first,last
John,Doe
Alice,Smith
"""
mock_accounts = pd.read_csv(StringIO(mock_accounts_data))

'''@patch('builtins.input', side_effect=['1', 'John', 'Doe', '2'])
@patch('components.login.accounts', mock_accounts)
def test_peopleSearch_existing_user(mock_input, capfd):
    # Mock the 'input' function to provide user input
    peopleSearch()
    out, _ = capfd.readouterr()
    
    assert "Would you like to connect with John Doe?" in out'''

@patch('builtins.input', side_effect=['1', 'Alice', 'Wonderland', '2'])
@patch('components.login.accounts', mock_accounts)
def test_peopleSearch_non_existing_user(mock_input, capfd):
    # Mock the 'input' function to provide user input
    peopleSearch()
    out, _ = capfd.readouterr()
    
    assert "Username was not found." in out

@patch('builtins.input', side_effect=['3', '2'])
def test_peopleSearch_return_to_search(mock_input, capfd):
    # Mock the 'input' function to provide user input
    peopleSearch()
    out, _ = capfd.readouterr()
    
    assert "Returning to People Search." in out

@patch('builtins.input', side_effect=['4', '2'])
def test_peopleSearch_invalid_option(mock_input, capfd):
    # Mock the 'input' function to provide user input
    peopleSearch()
    out, _ = capfd.readouterr()
    
    assert "Invalid option. Returning to People Search." in out
