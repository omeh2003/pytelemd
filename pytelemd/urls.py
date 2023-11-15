import re

from pytelemd.all_characters import replace_all_characters

REPLACE_IN_URL = [')']
def replace_urls(text):
    #must do it 4th
    pattern = r'\[(.*?)\]\((.*?)\)'

    _texts = []
    _links = []

    def replace_with_placeholder(match):
        _texts.append(match.group(1))
        _links.append(match.group(2))
        return "%url%"

    modified_text = re.sub(pattern, replace_with_placeholder, text)
    _new_texts = []
    for t in _texts:
        t = replace_all_characters(t)
        _new_texts.append(t)

    return modified_text, _new_texts, _links



