import re


def replace_inline_code_blocks_corrected(text):
    pattern = r'(?<!\\)(?:\\\\)*`(.*?)(?<!\\)(?:\\\\)*`'

    _inline_code_blocks = []

    def replace_with_placeholder(match):
        _inline_code_blocks.append('`' + match.group(1) + '`')
        return "%inlinecodeblock%"

    modified_text = re.sub(pattern, replace_with_placeholder, text)

    return modified_text, _inline_code_blocks
