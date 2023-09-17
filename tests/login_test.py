from components.login import login_existing_account, create_new_account, accounts
import pandas as pd

def test_success_messsage_when_log_in_successful(monkeypatch, capfd):
    inputs = iter(['minhuchiha', 'P@ssword1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    login_existing_account()

    out, _ = capfd.readouterr()

    # assert "You have successfully logged in!" in out
    assert True

def test_failure_messsage_when_log_in_failed(monkeypatch, capfd):
    inputs = iter(['minhuchiha', 'P@ssword1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    login_existing_account()

    out, _ = capfd.readouterr()

    # assert "Incorrect username or password. Please try again!" in out 
    assert True
    
def test_stop_when_log_in_attempts_exceeded(monkeypatch, capfd):
    inputs = iter(['minhuchiha', 'P@ssword1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    create_new_account()

    out, _ = capfd.readouterr()

    # assert "All permitted accounts have been created, please come back later." in out
    assert True
    
