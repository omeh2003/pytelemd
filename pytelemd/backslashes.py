NOT_REPLACE_CHARACTED = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']


def escape_backslashes_simple(text):
    #must do it 1st
    modified_text = ""

    for i in range(len(text)):
        if i + 1 > len(text):
            break
        if text[i] == '\\':

            if (i + 1 < len(text)) and (text[i + 1] not in NOT_REPLACE_CHARACTED) and (text[i + 1] != '\\'):
                modified_text += '\\'
        modified_text += text[i]

    return modified_text
