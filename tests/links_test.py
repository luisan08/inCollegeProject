from components.menu import display_inCollege_important_link, incollege_important_links_user_selection
from components.menu_helper import language_option 

def test_display_inCollege_important_link(capsys):
    display_inCollege_important_link()
    captured = capsys.readouterr()
    expected_output = (
        "\nInCollege Important Links:\n"
        "1. A Copyright Notice\n"
        "2. About\n"
        "3. Accessibility\n"
        "4. User Agreement\n"
        "5. Privacy Policy\n"
        "6. Cookie Policy\n"
        "7. Brand Policy\n"
        "8. Copyright Policy\n"
        "9. Languages\n"
        "10. Go Back to Previous Menu\n"
    )
    assert captured.out == expected_output

# @pytest.mark.parametrize("link_choice", ["1"])
# def test_incollege_important_links_user_selection(link_choice, monkeypatch, capsys):
#     monkeypatch.setattr('builtins.input', lambda _: link_choice)
#     with patch('components.menu.print') as mock_print:
#         incollege_important_links_user_selection()
#         captured = capsys.readouterr()
#     expected_output = "Copy right\n@ 2023 James Anderson LLC\n"
#     assert expected_output in captured.out
