from components.search import jobSearch, saveJob, applyJob
from unittest.mock import patch
from unittest import mock
import json

# Test job post
mock_jobs = [{
        "job_id": 6,
        "username": "MinhUchiha",
        "Title": "Machine Learning Engineer",
        "Description": "Develop ML Models",
        "Employer": "Google Deepmind",
        "Location": "Mountain View, CA",
        "Salary": "600000",
        "Applicants": []
    }]
@patch('builtins.input', side_effect=['1', 'Software Engineer', 'Develop software applications', 'ABC Inc.', 'New York', '80000', '3'])
@patch('components.search.jobs', mock_jobs)
@patch('components.config.Config.SYSTEM_ACCOUNT', ("Minh", "Pham", "MinhUchiha"))
@patch('components.config.Config.FLAG', True)
def test_jobSearch_post_job_success(_, capsys):
    # Call the jobSearch function
    jobSearch()

    # Get the output
    out, _ = capsys.readouterr()
    
    # Assertions
    assert "You have successfully posted a job!" in out # Assert the success message is printed out
    assert any(job["username"] == "MinhUchiha" and job["Title"] == "Software Engineer" and job["Description"] == "Develop software applications" and job["Employer"] == 'ABC Inc.' and job["Location"] == 'New York' and job["Salary"] == '80000' for job in mock_jobs) # Assert that the new job is inserted in jobs.json

# Test job deletion
mock_jobs_2 = [{
        "job_id": 6,
        "username": "MinhUchiha",
        "Title": "Machine Learning Engineer",
        "Description": "Develop ML Models",
        "Employer": "Google Deepmind",
        "Location": "Mountain View, CA",
        "Salary": "600000",
        "Applicants": []
    }]
@patch('builtins.input', side_effect=['2', '0', '3'])
@patch('components.search.jobs', mock_jobs_2)
@patch('components.config.Config.SYSTEM_ACCOUNT', ("Minh", "Pham", "MinhUchiha"))
@patch('components.config.Config.FLAG', True)
def test_jobSearch_delete_job_success(_, capfd):
    # Call the jobSearch function
    jobSearch()

    # Get the output
    out, _ = capfd.readouterr()

    # Assertions
    assert "You have successfully deleted a job!" in out # Success message should appear
    assert not mock_jobs_2 # The job should be deleted

# Only the person who posted the job can delete it
mock_jobs_3 = [{
        "job_id": 6,
        "username": "MinhUchiha",
        "Title": "Machine Learning Engineer",
        "Description": "Develop ML Models",
        "Employer": "Google Deepmind",
        "Location": "Mountain View, CA",
        "Salary": "600000",
        "Applicants": []
    }, {
        "job_id": 7,
        "username": "NotMinhUchiha",
        "Title": "Web Engineer",
        "Description": "Create UI Components",
        "Employer": "Uber",
        "Location": "Santa Clara, CA",
        "Salary": "180000",
        "Applicants": []
    }]
@patch('builtins.input', side_effect=['2', '0', '3'])
@patch('components.search.jobs', mock_jobs_3)
@patch('components.config.Config.SYSTEM_ACCOUNT', ("Minh", "Pham", "NotMinhUchiha"))
@patch('components.config.Config.FLAG', True)
def test_jobSearch_only_delete_user_posted_jobs(_, capfd):
    # Call the jobSearch function
    jobSearch()

    # Get the output
    out, _ = capfd.readouterr()

    # Assertions
    assert "You have successfully deleted a job!" in out # Success message should appear
    assert len(mock_jobs_3) == 1
    assert mock_jobs_3[0]["job_id"] == 6

# The number of job listings that the system can support is 10
mock_jobs_4 = [{
        "job_id": 1,
        "username": "MinhUchiha",
        "Title": "Machine Learning Engineer",
        "Description": "Develop ML Models",
        "Employer": "Google Deepmind",
        "Location": "Mountain View, CA",
        "Salary": "600000",
        "Applicants": []
    }, {
        "job_id": 2,
        "username": "Minh",
        "Title": "Machine Learning Engineer",
        "Description": "Develop ML Models",
        "Employer": "Google Deepmind",
        "Location": "Mountain View, CA",
        "Salary": "600000",
        "Applicants": []
    }, {
        "job_id": 3,
        "username": "Uchiha",
        "Title": "Machine Learning Engineer",
        "Description": "Develop ML Models",
        "Employer": "Google Deepmind",
        "Location": "Mountain View, CA",
        "Salary": "600000",
        "Applicants": []
    }, {
        "job_id": 4,
        "username": "MinhUchiha",
        "Title": "Machine Learning Engineer",
        "Description": "Develop ML Models",
        "Employer": "Google Deepmind",
        "Location": "Mountain View, CA",
        "Salary": "600000",
        "Applicants": []
    }, {
        "job_id": 5,
        "username": "MinhUchiha",
        "Title": "Machine Learning Engineer",
        "Description": "Develop ML Models",
        "Employer": "Google Deepmind",
        "Location": "Mountain View, CA",
        "Salary": "600000",
        "Applicants": []
    }, {
        "job_id": 6,
        "username": "MinhUchiha",
        "Title": "Machine Learning Engineer",
        "Description": "Develop ML Models",
        "Employer": "Google Deepmind",
        "Location": "Mountain View, CA",
        "Salary": "600000",
        "Applicants": []
    }, {
        "job_id": 7,
        "username": "MinhUchiha",
        "Title": "Machine Learning Engineer",
        "Description": "Develop ML Models",
        "Employer": "Google Deepmind",
        "Location": "Mountain View, CA",
        "Salary": "600000",
        "Applicants": []
    }, {
        "job_id": 8,
        "username": "MinhUchiha",
        "Title": "Machine Learning Engineer",
        "Description": "Develop ML Models",
        "Employer": "Google Deepmind",
        "Location": "Mountain View, CA",
        "Salary": "600000",
        "Applicants": []
    }, {
        "job_id": 9,
        "username": "MinhUchiha",
        "Title": "Machine Learning Engineer",
        "Description": "Develop ML Models",
        "Employer": "Google Deepmind",
        "Location": "Mountain View, CA",
        "Salary": "600000",
        "Applicants": []
    }]
@patch('builtins.input', side_effect=['1', 'Software Engineer', 'Develop software applications', 'ABC Inc.', 'New York', '80000', '1', '3'])
@patch('components.search.jobs', mock_jobs_4)
@patch('components.config.Config.SYSTEM_ACCOUNT', ("Minh", "Pham", "MinhUchiha"))
@patch('components.config.Config.FLAG', True)
def test_jobSearch_post_job_listings_can_not_exceed_ten(_, capsys):
    # Call the jobSearch function
    jobSearch()

    # Get the output
    out, _ = capsys.readouterr()
    
    # Assertions
    assert "You have successfully posted a job!" in out # Assert the success message is printed out
    assert any(job["username"] == "MinhUchiha" and job["Title"] == "Software Engineer" and job["Description"] == "Develop software applications" and job["Employer"] == 'ABC Inc.' and job["Location"] == 'New York' and job["Salary"] == '80000' for job in mock_jobs_4) # Assert that the 10th job is inserted in jobs
    assert len(mock_jobs_4) == 10
    assert "All permitted jobs have been created, please come back later." in out # Assert that the 11th job post can not be created

# When apply for a job, the listing of all jobs should be shown. In addition, success message should also be printed out when apply successfully
mock_jobs_5 = [{
        "job_id": 1,
        "username": "MinhUchiha",
        "Title": "Machine Learning Engineer",
        "Description": "Develop ML Models",
        "Employer": "Google Deepmind",
        "Location": "Mountain View, CA",
        "Salary": "600000",
        "Applicants": []
    }, {
        "job_id": 2,
        "username": "Minh",
        "Title": "Data Engineer",
        "Description": "Work with MLOps",
        "Employer": "OpenAI",
        "Location": "San Jose, CA",
        "Salary": "500000",
        "Applicants": [{'username': 'MinhUchiha', 'graduation_date' : '05/31/2025', 'start_working_date' : '05/28/2023', 'paragraph': 'Bla Bla Bla...', "appliedDate": "11/4/2023"}]
    }, {
        "job_id": 3,
        "username": "Uchiha",
        "Title": "Senior Machine Learning Engineer",
        "Description": "Develop ML Models",
        "Employer": "Adobe Firefly",
        "Location": "Lehi, Utah",
        "Salary": "450000",
        "Applicants": []
    }]
@patch('builtins.input', side_effect=['1', '05/31/2025', '05/28/2023', 'I have experience being a ML Engineer at prestigious companies like Palantir and OpenAI'])
@patch('components.search.jobs', mock_jobs_5)
@patch('components.config.Config.SYSTEM_ACCOUNT', ("Minh", "Pham", "NotMinhUchiha"))
@patch('components.config.Config.FLAG', True)
def test_apply_job_get_success_message_after_applying_and_save_applicant(_, capsys):
    # Call applyJob function
    applyJob()

    # Get stdout output from system
    out, _ = capsys.readouterr()
    
    # Assertions
    assert "You have successfully applied for a job!" in out # Success message is printed
    assert any(job['job_id'] == 1 and job['Applicants'][0]['username'] == 'NotMinhUchiha' for job in mock_jobs_5) # Assert that the applicants field was updated

# Once the user have applied for the job, they can not apply for it again 
mock_jobs_6 = [{
        "job_id": 1,
        "username": "MinhUchiha",
        "Title": "Machine Learning Engineer",
        "Description": "Develop ML Models",
        "Employer": "Google Deepmind",
        "Location": "Mountain View, CA",
        "Salary": "600000",
        "Applicants": []
    }, {
        "job_id": 2,
        "username": "Minh",
        "Title": "Data Engineer",
        "Description": "Work with MLOps",
        "Employer": "OpenAI",
        "Location": "San Jose, CA",
        "Salary": "500000",
        "Applicants": [{'username': 'MinhUchiha', 'graduation_date' : '05/31/2025', 'start_working_date' : '05/28/2023', 'paragraph': 'Bla Bla Bla...', "appliedDate": "11/7/2023"}]
    }, {
        "job_id": 3,
        "username": "Uchiha",
        "Title": "Senior Machine Learning Engineer",
        "Description": "Develop ML Models",
        "Employer": "Adobe Firefly",
        "Location": "Lehi, Utah",
        "Salary": "450000",
        "Applicants": []
    }]
@patch('builtins.input', side_effect=['2'])
@patch('components.search.jobs', mock_jobs_6)
@patch('components.config.Config.SYSTEM_ACCOUNT', ("Minh", "Pham", "MinhUchiha"))
@patch('components.config.Config.FLAG', True)
def test_can_not_apply_for_a_job_that_has_been_applied(_, capsys):
    # Call applyJob function
    applyJob()

    # Get stdout output from system
    out, _ = capsys.readouterr()
    
    # Assertions
    assert "You have already applied for this job." in out # Success message is printed

# Get listing of the titles of all jobs in the system
mock_jobs_7 = [{
        "job_id": 1,
        "username": "MinhUchiha",
        "Title": "Machine Learning Engineer",
        "Description": "Develop ML Models",
        "Employer": "Google Deepmind",
        "Location": "Mountain View, CA",
        "Salary": "600000",
        "Applicants": []
    }, {
        "job_id": 2,
        "username": "Minh",
        "Title": "Data Engineer",
        "Description": "Work with MLOps",
        "Employer": "OpenAI",
        "Location": "San Jose, CA",
        "Salary": "500000",
        "Applicants": [{'username': 'MinhUchiha', 'graduation_date' : '05/31/2025', 'start_working_date' : '05/28/2023', 'paragraph': 'Bla Bla Bla...', "appliedDate": "11/4/2023"}]
    }, {
        "job_id": 3,
        "username": "Uchiha",
        "Title": "Senior Machine Learning Engineer",
        "Description": "Develop ML Models",
        "Employer": "Adobe Firefly",
        "Location": "Lehi, Utah",
        "Salary": "450000",
        "Applicants": []
    }]
@patch('builtins.input', side_effect=['1', '05/31/2025', '05/28/2023', 'I have experience being a ML Engineer at prestigious companies like Palantir and OpenAI'])
@patch('components.search.jobs', mock_jobs_7)
@patch('components.config.Config.SYSTEM_ACCOUNT', ("Minh", "Pham", "NotMinhUchiha"))
@patch('components.config.Config.FLAG', True)
def test_apply_job_get_listing_of_all_jobs(_, capsys):
    # Call applyJob function
    applyJob()

    # Get stdout output from system
    out, _ = capsys.readouterr()
    
    # Assertions
    # Success message is printed
    assert "1. Machine Learning Engineer\nDescription: Develop ML Models\nEmployer: Google Deepmind\nLocation: Mountain View, CA\nSalary: 600000" in out 
    assert "2. Data Engineer\nDescription: Work with MLOps\nEmployer: OpenAI\nLocation: San Jose, CA\nSalary: 500000" in out 
    assert "3. Senior Machine Learning Engineer\nDescription: Develop ML Models\nEmployer: Adobe Firefly\nLocation: Lehi, Utah\nSalary: 450000" in out 

# def test_saveJob():
#     # Create a dummy profile JSON file
#     dummy_profile = {
#         'user123': {
#             'SavedJobs': [1, 2],
#         }
#     }
    
#     # Create a dummy jobs list
#     dummy_jobs = [
#         {
#             'job_id': 1,
#             'Title': 'Job 1',
#         },
#         {
#             'job_id': 2,
#             'Title': 'Job 2',
#         }
#     ]

#     # Mock the reading of the profile JSON file
#     with mock.patch('builtins.open', mock.mock_open(read_data=json.dumps(dummy_profile))):
#         # Mock the reading of the jobs JSON file
#         with mock.patch('builtins.open', mock.mock_open(read_data=json.dumps(dummy_jobs))):

#             # Ensure the user can successfully save a job
#             assert saveJob('user123', 3) == "You have successfully saved a job!"

#             # Ensure the user cannot save the same job twice
#             assert saveJob('user123', 1) == "You have already saved this job."

#             # Ensure the user cannot save their own job
#             assert saveJob('user123', 4) == "You cannot save your own job."

#             # Ensure the user cannot save a job that doesn't exist
#             assert saveJob('user123', 5) == "The selected job does not exist."

#             # Ensure the user cannot save a job without a valid username
#             assert saveJob(None, 3) == "Invalid username."

#             # Ensure the user cannot save a job without a valid job_id
#             assert saveJob('user123', None) == "Invalid job ID."



