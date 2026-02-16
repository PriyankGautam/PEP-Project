# def remove_html_chars(text):
#     """

#     Removes HTML-related characters: <, >, /
    
#     """ (function) def help_menu()-> None
#         This is the help menu The package has 3 methods
#     print(help_menu.__doc__)

# def remove_char(bad_stuff,input_string):
#     return input_string.replace(bad_stuff, '')
# def help_menu(html_input: str) -> str:
#     for char in ['<', '>', '/']:
#         html_input = html_input.replace(char, '')
#     return html_input

def remove_html_chars(text: str) -> str:
    """
    Removes HTML-related characters: <, >, /
    """
    for char in ['<', '>', '/']:
        text = text.replace(char, '')
    return text


def remove_char(bad_stuff: str, input_string: str) -> str:
    """
    Removes a specific character from the input string
    """
    return input_string.replace(bad_stuff, '')


def help_menu() -> None:
    """
    Help Menu:
    This package has 3 methods:
    1. remove_html_chars(text)
    2. remove_char(bad_stuff, input_string)
    3. help_menu()
    """
    print(help_menu.__doc__)
