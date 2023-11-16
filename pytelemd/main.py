import re

from pytelemd.all_characters import replace_all_characters
from pytelemd.backslashes import escape_backslashes_simple
from pytelemd.code_blocks import replace_code_blocks
from pytelemd.inline_code_blocks import replace_inline_code_blocks_corrected
from pytelemd.urls import replace_urls


# Process the string
def process_string(text):
    _ = escape_backslashes_simple(text)
    _, code_blocks = replace_code_blocks(_)
    _, inline_code_blocks = replace_inline_code_blocks_corrected(_)
    _, title, link = replace_urls(_)
    _ = replace_all_characters(_)
    return _, code_blocks, inline_code_blocks, title, link

def replace_placeholders(text, list, placeholder):
    lists = iter(list)
    placeholder = r'%' + placeholder + r'%'

    def replace_with(match):
        try:
            return next(lists)
        except StopIteration:
            return match.group(0)

    modified_text = re.sub(placeholder, replace_with, text)

    return modified_text


def corect_md(text):
    modifer_text, code_blocks, inline_code_blocks, title, link = process_string(text)
    restract_text_code = replace_placeholders(modifer_text, code_blocks, 'codeblock')
    restract_text_code_inline = replace_placeholders(restract_text_code, inline_code_blocks, 'inlinecodeblock')
    urls=[]
    for i in range(len(title)):
        urls.append(f'[{title[i]}]({link[i]})')
    restract_text_url = replace_placeholders(restract_text_code_inline, urls, 'url')
    return restract_text_url

