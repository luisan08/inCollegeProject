import pandas as pd
from unittest.mock import patch, MagicMock, call
import builtins
import io
import pytest
from components.friends import (
    friends,
    disconnect,
    show_my_network,
    reject_request,
    accept_request,
    notifications,
    process_request,
    find_someone,
    send_request
    )

# --------------------------Friends Functions Tests Mock Data--------------------------

class MockConfig:
    FLAG = False

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

# --------------------------Friends Functions Tests--------------------------
@patch('components.friends.Config', MockConfig)
def test_friends():
    pass

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
    
def test_reject_request():
    pass

def test_accept_request():
    pass

def test_notifications():
    pass

def test_process_request():
    pass

def test_find_someone():
    pass

def test_send_request():
    pass

