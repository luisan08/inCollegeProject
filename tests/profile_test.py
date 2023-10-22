import json
import pytest
from unittest.mock import mock_open, patch
from components.profile import create_profile, view_profile, view_friend_profile, profile
from components.login import login


#-------------------------------- view profile test --------------------------------
"""
def test_view_profile_existing_user(capsys):
    # Mock the 'open' function and the file content
    mock_data = {
        "user_profile": {
            "title": "3rd year Computer Science Student",
            "major": "Computer Science",
            "university": "University Of South Florida",
            "about": "Aspiring developer.",
            "experience": [
                {
                    "title": "web developer",
                    "employer": "Apple",
                    "date_start": "10/10/24",
                    "date_end": "10/20/26",
                    "location": "Florida",
                    "description": "Develop a website."
                },
                {
                    "title": "Software engineer",
                    "employer": "Microsoft",
                    "date_start": "1/12/2021",
                    "date_end": "21/12/2023",
                    "location": "New York",
                    "description": "Bug fixes."
                }
            ],
            "education": [
                {
                    "school": "University Of South Florida",
                    "degree": "Bachelor In Computer Science",
                    "year_attended": "2020"
                }
            ]
        }
    }
    mock_file = json.dumps(mock_data)
    with patch("builtins.open", new_callable=mock_open, read_data=mock_file):
        view_profile("user_profile")
        captured = capsys.readouterr()

    expected_output = \nuser_profile's Profile:
Title: 3rd Year Computer Science Student
Major: Computer Science
University: University Of South Florida
About: Aspiring developer

Experiences:
  Title: web developer
  Employer: Apple
  Date Started: 10/10/24
  Date Ended: 10/20/26
  Location: Florida
  Description: Develop a website

  Title: Software engineer
  Employer: Microsoft
  Date Started: 1/12/2021
  Date Ended: 21/12/2023
  Location: New York
  Description: Bug fixes

Education:
  School: University Of South Florida
  Degree: Bachelor In Computer Science
  Year Attended: 2020


    assert captured.out.strip() == expected_output.strip()


def test_view_profile_non_existing_user(capsys):
    # Mock the 'open' function and the file content
    mock_data = {}
    mock_file = json.dumps(mock_data)
    with patch("builtins.open", new_callable=mock_open, read_data=mock_file):
        view_profile("non_existing_user")
        captured = capsys.readouterr()
        
    expected_output = "You don't have a profile. Create one using 'create_profile'.\n"
    assert captured.out == expected_output

"""

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



#---------------------- view profile test -------------------------------






