from components.search import jobSearch, peopleSearch, skillSearch
import pytest

def test_job_search(capfd):
    jobSearch()
    out, _ = capfd.readouterr()
    assert "Under construction." in out

def test_people_search(capfd):
    peopleSearch()
    out, _ = capfd.readouterr()
    assert "Under construction." in out

@pytest.mark.parametrize("skillChoice",[1, 2, 3, 4, 5])
def test_skill_search(skillChoice, monkeypatch, capfd):
    monkeypatch.setattr('builtins.input', lambda _: skillChoice)
    skillSearch()
    out, _ = capfd.readouterr()
    assert "Under construction." in out