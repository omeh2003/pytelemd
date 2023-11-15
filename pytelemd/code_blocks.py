import re



def escape_backticks(text):
    # Pattern to find non-escaped backticks
    # A backtick is considered non-escaped if it is not preceded by an odd number of backslashes
    pattern = r'(?<!\\)(?:\\\\)*`'
    modified_text = []
    # Replace non-escaped backticks with escaped backticks
    for line in text:
        modified_text.append(re.sub(pattern, r'\\`', line))

    return modified_text
def replace_code_blocks(text):
    #must do it 2nd
    pattern = r'```(.+?)```'

    _code_blocks = []

    def replace_with_placeholder(match):
        _code_blocks.append(match.group(1))
        return "%codeblock%"

    modified_text = re.sub(pattern, replace_with_placeholder, text, flags=re.DOTALL)

    _code_blocks= escape_backticks(_code_blocks)
    _new_code_blocks = []
    for i in range(len(_code_blocks)):
        _new_code_blocks.append("```" + _code_blocks[i] + "```")

    return modified_text, _new_code_blocks
