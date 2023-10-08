import pandas as pd
import json
from unittest.mock import patch, MagicMock, call
import builtins
import io
import pytest
from components.friends import (
    friends,
    disconnect,
    show_my_network,
    notifications,
    process_request,
    find_someone,
    send_request
    )

# --------------------------Function disconnect--------------------------
class MockConfig:
    FLAG = False
    SYSTEM_ACCOUNT = ["System", "Account", "user1"]

mocked_friendLists = [
    {
        "user1": {
            "friendList": ["user2", "user3"],
            "pendingRequest": []
        }
    },
    {
        "user2": {
            "friendList": ["user1"],
            "pendingRequest": []
        }
    },
    {
        "user3": {
            "friendList": ["user1"],
            "pendingRequest": []
        }
    },
    {
        "user4": {
            "friendList": [],
            "pendingRequest": []
        }
    }
]

@patch('components.friends.friendLists', mocked_friendLists)
@patch('builtins.open', new_callable=MagicMock)
@patch('json.dump')
def test_disconnect_success(mock_json_dump, mock_open, capsys):
    from components.friends import disconnect

    # Test disconnection success
    result = disconnect("user1", "user2")
    
    assert result is True
    mock_json_dump.assert_called_once_with(mocked_friendLists, mock_open.return_value.__enter__.return_value)
    assert "user2" not in mocked_friendLists[0]["user1"]["friendList"]
    assert "user1" not in mocked_friendLists[1]["user2"]["friendList"]

@patch('components.friends.friendLists', mocked_friendLists)
@patch('builtins.open', new_callable=MagicMock)
@patch('json.dump')
@patch('builtins.print')
def test_disconnect_failure(mock_print, mock_json_dump, mock_open, capsys):
    from components.friends import disconnect

    # Test disconnection failure (friend does not exist)
    result = disconnect("user1", "non_existent_user")
    
    assert result is False
    mock_json_dump.assert_not_called()
    mock_print.assert_called_once_with("You are not connected with this user.")

@patch('components.friends.friendLists', mocked_friendLists)
def test_show_my_network(capsys):
    from components.friends import show_my_network  

    show_my_network("user1")

    captured = capsys.readouterr()
    assert "Your network:\nuser3\n" in captured.out

    show_my_network("user4")
    captured = capsys.readouterr()
    assert ("You don't have any connections yet.") in captured.out

# --------------------------Function notifications--------------------------
mocked_friendLists_noti = [
    {
        "user1": {
            "friendList": ["user2"],
            "pendingRequest": ["user3"]
        }
    },
    {
        "user2": {
            "friendList": ["user1"],
            "pendingRequest": []
        }
    },
    {
        "user3": {
            "friendList": [],
            "pendingRequest": []
        }
    }
]

mocked_accounts_noti = pd.DataFrame({
    'username': ['user1', 'user2', 'user3'],
    'first': ['User', 'Another', 'Third'],
    'last': ['One', 'User', 'User']
})

@patch('components.friends.friendLists', mocked_friendLists_noti)
@patch('components.friends.accounts', mocked_accounts_noti)
@patch('components.friends.Config', MockConfig)
@patch('builtins.open', new_callable=MagicMock)
@patch('json.dump')
@patch('builtins.input')
def test_notifications(mock_input, mock_json_dump, mock_open, capsys):
    from components.friends import notifications
    
    mock_input.side_effect = [
        '0',  # Choose the first request
        '1',  # Accept the request
        'q'   # Quit
    ]

    def mock_process_request_side_effect(*args, **kwargs):
        print(f"mock_process_request called with: {args}, {kwargs}")

    with patch('components.friends.process_request', side_effect=mock_process_request_side_effect) as mock_process_request:
        notifications("user1")

    print(f"process_request called: {mock_process_request.called}")
    print(f"call args: {mock_process_request.call_args}")
    print(f"call count: {mock_process_request.call_count}")

    mock_process_request.assert_called_once_with('user3', 'user1')

    assert 'user3' not in mocked_friendLists[0]['user1']['pendingRequest']

    mock_json_dump.assert_called_once_with(mocked_friendLists_noti, mock_open.return_value.__enter__.return_value)

# --------------------------Function process_request--------------------------
mocked_friendLists_process_request = [
    {
        "user1": {
            "friendList": [],
            "pendingRequest": []
        }
    },
    {
        "user2": {
            "friendList": [],
            "pendingRequest": []
        }
    },
    {
        "user3": {
            "friendList": [],
            "pendingRequest": []
        }
    }
]

@patch('components.friends.friendLists', mocked_friendLists_process_request)
@patch('builtins.open', new_callable=MagicMock)
@patch('json.dump')
def test_process_request(mock_json_dump, mock_open):
    from components.friends import process_request  

    process_request("user2", "user1")
    
    assert "user1" in mocked_friendLists_process_request[1]["user2"]["friendList"]
    
    assert "user2" in mocked_friendLists_process_request[0]["user1"]["friendList"]

    print(mock_json_dump.call_args_list)
    mock_json_dump.assert_called_once_with(mocked_friendLists_process_request, mock_open.return_value.__enter__.return_value)

# --------------------------Function find_someone--------------------------
mocked_accounts = pd.DataFrame({
    'username': ['user1', 'user2', 'user3'],
    'first': ['Alice', 'Bob', 'Charlie'],
    'last': ['Johnson', 'Smith', 'Doe'],
    'university': ['Uni1', 'Uni2', 'Uni3'],
    'major': ['Major1', 'Major2', 'Major3']
})

class MockConfig:
    SYSTEM_ACCOUNT = [None, None, 'user1']

@pytest.fixture
def mock_send_request():
    with patch('components.friends.send_request', autospec=True) as mock:
        yield mock

@patch('components.friends.Config', MockConfig)
@patch('components.friends.accounts', mocked_accounts)
@patch('builtins.input')
def test_find_someone(mock_input, mock_send_request, capsys):
    from components.friends import find_someone 
    
    mock_input.side_effect = [
        'Smith',  # Last name
        'Uni2',  # University
        'Major2',  # Major
        '1',  # Choose person to connect
        'e'  # Exit
    ]
    
    find_someone()
    
    captured = capsys.readouterr()
    assert 'Here are the results for your search: \n  First Name Last Name University   Major\n0        Bob     Smith       Uni2  Major2\n1    Charlie       Doe       Uni3  Major3\nSent request to Charlie Doe!' in captured.out


# --------------------------Function send request--------------------------
mocked_friendLists_send_request = [
    {
        "user1": {
            "friendList": ["user2"],
            "pendingRequest": []
        }
    },
    {
        "user2": {
            "friendList": ["user1"],
            "pendingRequest": []
        }
    }
]

MockConfig = MagicMock()
MockConfig.SYSTEM_ACCOUNT = ['system_user', 'password', 'user1']

@patch('components.friends.friendLists', mocked_friendLists_send_request)
@patch('components.friends.Config', MockConfig)
@patch('builtins.open', new_callable=MagicMock)
@patch('json.dump')
def test_send_request(mock_json_dump, mock_open):
    from components.friends import send_request  
    
    send_request("user2")
    print(mocked_friendLists_send_request[1]["user2"]["pendingRequest"])

    assert 'user1' in mocked_friendLists_send_request[1]["user2"]["pendingRequest"]
    
    mock_json_dump.assert_called_once_with(mocked_friendLists_send_request, mock_open.return_value.__enter__.return_value)

