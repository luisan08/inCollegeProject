import json
import pytest
from unittest.mock import mock_open, patch
from components.profile import create_profile, view_profile, view_friend_profile, profile



#---------------------------view friend profile test ---------------------------------------

def test_view_friend_profile_existing_user(capsys):
    # Mock the 'open' function and the file content
    mock_data = {
        "username1": {
            "title": "test",
            "major": "Major",
            "university": "University",
            "about": "test about",
            "experience": [
                {
                    "title": "test experience",
                    "employer": "Test",
                    "date_start": "test start date",
                    "date_end": "test end date",
                    "location": "Location",
                    "description": "test description",
                }
            ],
            "education": [
                {
                    "school": "test school",
                    "degree": "test degree",
                    "year_attended": "2020"
                }
            ]
        }
    }
     
    mock_file = json.dumps(mock_data)
    with patch("builtins.open", new_callable=mock_open, read_data=mock_file):
        view_friend_profile("username1")
        captured = capsys.readouterr()

    expected_output = """
\nFriend's Profile:
Title: test
Major: Major
University: University
About: test about

Experiences:
  Title: test experience
  Employer: Test
  Date Started: test start date
  Date Ended: test end date
  Location: Location
  Description: test description

Education:
  School: test school
  Degree: test degree
  Year Attended: 2020
"""

    assert captured.out.strip() == expected_output.strip()

def test_view_friend_profile_non_existing_user(capsys):
    # Mock the 'open' function and the file content
    mock_data = {}
    mock_file = json.dumps(mock_data)
    with patch("builtins.open", new_callable=mock_open, read_data=mock_file):
        view_friend_profile("non_existing_user")
        captured = capsys.readouterr()
        
    expected_output = "This friend does not have a profile.\n"
    assert captured.out == expected_output

#----------------------create profile test --------------------------------

def test_create_profile_title(capsys):
    mock_data = {}
    with patch("builtins.open", new_callable=mock_open, read_data=json.dumps(mock_data)):
        with patch("builtins.input", side_effect=["1", "My Title", "7"]):
            create_profile("user1")
        captured = capsys.readouterr()
        
    assert "Title section updated successfully." in captured.out

def test_create_profile_major(capsys):
    mock_data = {}
    with patch("builtins.open", new_callable=mock_open, read_data=json.dumps(mock_data)):
        with patch("builtins.input", side_effect=["2", "Computer Science", "7"]):
            create_profile("user1")
        captured = capsys.readouterr()
        
    assert "Major section updated successfully." in captured.out

def test_create_profile_university(capsys):
    mock_data = {}
    with patch("builtins.open", new_callable=mock_open, read_data=json.dumps(mock_data)):
        with patch("builtins.input", side_effect=["3", "University of XYZ", "7"]):
            create_profile("user1")
        captured = capsys.readouterr()
        
    assert "University section updated successfully." in captured.out
def test_create_profile_about(capsys):
    mock_data = {}
    with patch("builtins.open", new_callable=mock_open, read_data=json.dumps(mock_data)):
        with patch("builtins.input", side_effect=["4", "This is my about section.", "7"]):
            create_profile("user1")
        captured = capsys.readouterr()

    assert "About section updated successfully." in captured.out

def test_create_profile_education(capsys):
    mock_data = {}
    with patch("builtins.open", new_callable=mock_open, read_data=json.dumps(mock_data)):
        with patch("builtins.input", side_effect=["6", "2", "USF University", "MBA", "2017-2019", "MIT University", "Ph.D.", "2015-2017", "7"]):
            create_profile("user1")
        captured = capsys.readouterr()

    assert "Education section updated successfully." in captured.out

def test_create_profile_experience(capsys):
    mock_data = {}
    with patch("builtins.open", new_callable=mock_open, read_data=json.dumps(mock_data)):
        with patch("builtins.input", side_effect=["5", "2", "Software Engineer", "Google", "2019", "2022", "Mountain View", "Worked on search algorithms.", "Data Analyst", "Facebook", "2017", "2019", "Menlo Park", "Analyzed user data.", "7"]):
            create_profile("user1")
        captured = capsys.readouterr()

    assert "Experience section updated successfully." in captured.out



#-------------------------------- view profile test --------------------------------


def test_view_profile_non_existing_user(capsys):
    # Mock the 'open' function and the file content
    mock_data = {}
    mock_file = json.dumps(mock_data)
    with patch("builtins.open", new_callable=mock_open, read_data=mock_file):
        view_profile("non_existing_user")
        captured = capsys.readouterr()
        
    expected_output = "You don't have a profile. Create one using 'create_profile'.\n"
    assert captured.out == expected_output







