REPLACE_CHARACTED = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']


def replace_all_characters(text):
    # must do it 5th
    modified_text = r''

    for i in range(len(text)):
        if text[i] in REPLACE_CHARACTED and (i - 1 >= 0) and (text[i - 1] != '\\'):
            modified_text += '\\'
        modified_text += text[i]

    return modified_text
