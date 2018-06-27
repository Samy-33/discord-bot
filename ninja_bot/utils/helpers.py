from bs4 import BeautifulSoup as bs


def empty_string_if_none(string: str):
    return string if string else ''

def remove_html_from_string(string: str):
    soup = bs(string, 'html.parser')
    return soup.text