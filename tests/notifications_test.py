import json
from unittest.mock import patch, mock_open, MagicMock
from components.notifications import (
    no_profile_notif, 
    message_notif, 
    reminder_jobs,
    notify_applied_jobs,
    deleted_job,
    new_job,
    new_student,
)

@patch('components.notifications.profiles', {'username1': {'some_profile_data'}})
def test_no_profile_notification(monkeypatch, capfd):
    no_profile_notif('username2')
    out, _ = capfd.readouterr()
    assert "\nDon't forget to create a profile." in out

    no_profile_notif('username1')
    out, _ = capfd.readouterr()
    assert "\nDon't forget to create a profile." not in out

@patch('components.notifications.messages', [{'username2': {'inbox': [{'read': False}]}}])
def test_new_message_notification(monkeypatch, capfd):
    message_notif('username2')
    out, _ = capfd.readouterr()
    assert "\nYou have a new messages waiting for you " in out

@patch('components.notifications.jobs', [{'Applicants': [{'username': 'username1', 'appliedDate': '01/01/2023'}]}])
def test_job_application_reminder(monkeypatch, capfd):
    reminder_jobs('username1')
    out, _ = capfd.readouterr()
    assert 'Remember – you\'re going to want to have a job when you graduate.' in out

@patch('components.notifications.jobs', [{'Applicants': [{'username': 'username1'}]}])
def test_notify_applied_jobs(monkeypatch, capfd):
    num_applied_jobs = notify_applied_jobs('username1')
    out, _ = capfd.readouterr()
    assert "\nYou have currently applied for 1 job." in out
    assert num_applied_jobs == 1

def test_deleted_job_notification(monkeypatch, capfd):
    mock_notifications_data = json.dumps({
        "username1": {
            "deletedJobs": ["Job1", "Job2"]
        }
    })

    with patch("builtins.open", mock_open(read_data=mock_notifications_data)):
        deleted_job("username1") 

        out, _ = capfd.readouterr()

        assert "\nThe job named Job1 that you applied for has been deleted." in out
        assert "\nThe job named Job2 that you applied for has been deleted." in out

@patch('components.notifications.jobs', [{'Title': 'New Job', 'Applicants': []}])
def test_new_job_notification(monkeypatch, capfd):
    new_job('username2')
    out, _ = capfd.readouterr()
    assert "\nA new job 'New Job' has been posted." in out

def test_new_student_notification(monkeypatch, capfd):
    mock_notifications_data = json.dumps({
        "username1": {
            "student": [
                {"first": "John", "last": "Doe"},
                {"first": "Jane", "last": "Smith"}
            ]
        }
    })

    mock_file = mock_open(read_data=mock_notifications_data)
    mock_file.return_value.__iter__ = lambda self: iter(self.readline, '')
    mock_file.return_value.write = MagicMock()

    with patch("builtins.open", mock_file):
        new_student("username1")  
        out, _ = capfd.readouterr()

        write_calls = mock_file.return_value.write.call_args_list
        written_data = ''.join(call_args[0][0] for call_args in write_calls)

        updated_notifications = json.loads(written_data)
        assert updated_notifications["username1"]["student"] == []