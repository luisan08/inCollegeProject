from components.login import login_existing_account, create_new_account
from unittest.mock import patch
import pandas as pd

@patch('components.login.accounts', pd.DataFrame({'username': ['minhuchiha', 'sdaffew'], 'password': ['P@ssword1', '1232sfs@Asd']}))
def test_success_messsage_when_log_in_successful(monkeypatch, capfd):
    inputs = iter(['minhuchiha', 'P@ssword1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    login_existing_account()
    out, _ = capfd.readouterr()

    assert "You have successfully logged in!" in out

@patch('components.login.accounts', pd.DataFrame({'username': ['minhuchiha', 'sdaffew'], 'password': ['P@ssword2', '1232sfs@Asd']}))
def test_failure_messsage_when_log_in_failed(monkeypatch, capfd):
    inputs = iter(['minhuchiha', 'P@ssword1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    out = ""
    try:
        login_existing_account()
    except StopIteration:
        out, _ = capfd.readouterr()
            
    assert "Incorrect username or password. Please try again!" in out 

@patch('components.login.accounts', pd.DataFrame({'username': ['minhuchiha', 'sdaffew', "asfsf", "dasd2343s", "adgrgre"], 'password': ['P@ssword2', '1232sfs@Asd', '12fs@Asd', '123$Asd', '132sfs@Asd']}))    
def test_stop_when_log_in_attempts_exceeded(monkeypatch, capfd):
    inputs = iter(['username', 'P@234fssword1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    create_new_account()

    out, _ = capfd.readouterr()

    assert "All permitted accounts have been created, please come back later." in out
    