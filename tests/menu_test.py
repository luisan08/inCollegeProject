from components.menu import *
from components.menu_helper import *
from unittest.mock import MagicMock, PropertyMock
from unittest.mock import patch
import pandas as pd
import pytest

# --------------------------Display Functions Tests--------------------------

def test_display_groups_of_links(capsys):
    display_groups_of_links()
    captured = capsys.readouterr()
    assert "\n1. Useful Links" in captured.out
    assert "2. InCollege Important Links" in captured.out
    assert "3. Exit menu" in captured.out

def test_display_useful_links(capsys):
    display_useful_links()
    captured = capsys.readouterr()
    assert "\nUseful Links:" in captured.out
    assert "1. General" in captured.out
    assert "2. Browse InCollege" in captured.out
    assert "3. Business Solutions" in captured.out
    assert "4. Directories" in captured.out
    assert "5. Go Back to Previous Menu" in captured.out

def test_display_inCollege_important_link(capsys):
    display_inCollege_important_link()
    captured = capsys.readouterr()
    assert "\nInCollege Important Links:" in captured.out
    assert "1. A Copyright Notice" in captured.out
    assert "2. About" in captured.out
    assert "3. Accessibility" in captured.out
    assert "4. User Agreement" in captured.out
    assert "5. Privacy Policy" in captured.out
    assert "6. Cookie Policy" in captured.out
    assert "7. Brand Policy" in captured.out
    assert "8. Copyright Policy" in captured.out
    assert "9. Languages" in captured.out
    assert "10. Go Back to Previous Menu" in captured.out

def test_display_general_links_not_logged_in(capsys):
    display_general_links(isLogin=False)
    captured = capsys.readouterr()
    assert "\nGeneral Links:" in captured.out
    assert "1. Sign Up" in captured.out
    assert "2. Help Center" in captured.out
    assert "3. About" in captured.out
    assert "4. Press" in captured.out
    assert "5. Blog" in captured.out
    assert "6. Careers" in captured.out
    assert "7. Developers" in captured.out
    assert "8. Go Back to Previous Menu" in captured.out

def test_display_general_links_logged_in(capsys):
    display_general_links(isLogin=True)
    captured = capsys.readouterr()
    assert "\nGeneral Links:" in captured.out
    assert "1. Sign Out" in captured.out
    assert "2. Help Center" in captured.out
    assert "3. About" in captured.out
    assert "4. Press" in captured.out
    assert "5. Blog" in captured.out
    assert "6. Careers" in captured.out
    assert "7. Developers" in captured.out
    assert "8. Go Back to Previous Menu" in captured.out

# --------------------------Selection Functions Tests--------------------------
class MockConfig:
    FLAG = True
    SYSTEM_ACCOUNT = ('John', 'Doe')

@pytest.mark.parametrize("input_choice, expected_output", [
    ('1', "\nUseful Links:\n1. General\n2. Browse InCollege\n3. Business Solutions\n4. Directories\n5. Go Back to Previous Menu\n\nGeneral Links:\n1. Sign Up\n2. Help Center\n3. About\n4. Press\n5. Blog\n6. Careers\n7. Developers\n8. Go Back to Previous Menu\n"),
    ('2', "\nUseful Links:\n1. General\n2. Browse InCollege\n3. Business Solutions\n4. Directories\n5. Go Back to Previous Menu\n\nUnder construction\n"),
    ('3', "\nUseful Links:\n1. General\n2. Browse InCollege\n3. Business Solutions\n4. Directories\n5. Go Back to Previous Menu\n\nUnder construction\n"),
    ('4', "\nUseful Links:\n1. General\n2. Browse InCollege\n3. Business Solutions\n4. Directories\n5. Go Back to Previous Menu\n\nUnder construction\n"),
    ('5', "\nUseful Links:\n1. General\n2. Browse InCollege\n3. Business Solutions\n4. Directories\n5. Go Back to Previous Menu\n"),
    ('6', "\nUseful Links:\n1. General\n2. Browse InCollege\n3. Business Solutions\n4. Directories\n5. Go Back to Previous Menu\n\nInvalid choice. Please try again.\n")
])
def test_useful_links_user_selection(monkeypatch, capsys, input_choice, expected_output):
    if input_choice == '1':
        inputs = [input_choice, "8", "5"]
    else:
        inputs = [input_choice, "5"]
    input_generator = (i for i in inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_generator))
    try:
        useful_links_user_selection()
    except StopIteration:
        captured = capsys.readouterr()
        assert captured.out == expected_output

# --------------------------Helper Functions Tests--------------------------
# Sample data to mock the CSV content
mocked_accounts_controls = pd.DataFrame({
    'first': [MockConfig.SYSTEM_ACCOUNT[0]],
    'last': [MockConfig.SYSTEM_ACCOUNT[1]],
    'sms': [True],
    'email': [False],
    'advertising': [True],
    'language': ['English']
})

# For patching pd.read_csv
mocked_pd_read_csv = patch('components.menu_helper.pd.read_csv', return_value=mocked_accounts_controls)

# For patching Config.SYSTEM_ACCOUNT
mocked_system_account = patch('components.menu_helper.Config.SYSTEM_ACCOUNT', new_callable=PropertyMock, return_value=MockConfig.SYSTEM_ACCOUNT)

@pytest.mark.parametrize("feature, feature_name, input_choice, expected_output", [
    (True, "SMS", "1", "SMS is on. \nPress 1 to turn it off. \nPress 2 to exit.\n"),
    (False, "InCollege email", "2", "InCollege email is off. \nPress 1 to turn it on. \nPress 2 to exit.\n")
])
def test_TurnOnOff(monkeypatch, capfd, feature, feature_name, input_choice, expected_output):
    monkeypatch.setattr('builtins.input', lambda _: input_choice)
    TurnOnOff(feature, feature_name)
    out, _ = capfd.readouterr()
    assert expected_output in out

mocked_accounts_controls_data = (
    mocked_accounts_controls, 
    0,
    mocked_accounts_controls.iloc[0]
)

@patch('components.menu_helper.accounts_controls', mocked_accounts_controls)
@patch('components.menu_helper.Config', MockConfig)
def test_guest_controls_selection(monkeypatch, capfd):
    with patch.object(pd.DataFrame, "to_csv", MagicMock()):
        # This test checks that turning off an already "on" SMS feature works as expected
        inputs = iter(["2", "1", "4"])  # choose SMS, turn off, exit
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        guest_controls_selection()
        out, _ = capfd.readouterr()
        assert "SMS is on. \nPress 1 to turn it off. \nPress 2 to exit." in out


@patch('components.menu_helper.accounts_controls', mocked_accounts_controls)
@patch('components.menu_helper.Config', MockConfig)
def test_language_option(monkeypatch, capfd):
    # This test sets language to Spanish
    inputs = iter(["2", "3"])  # choose Spanish, exit
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    language_option()
    out, _ = capfd.readouterr()
    assert "\nLanguage was set to Spanish" in out