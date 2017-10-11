#!/bin/python3
# -*- coding: utf-8 -*-

import pysrt
import re


__all__ = ['filter_function_ted']

def filter_function_ted(subs):
    text = []
    for line in subs:
        filtered = re.sub(r'\n', ' ', line.text)
        filtered = re.sub(r'\([^)]*\)', ' ', filtered)
        filtered = re.sub(r'&nbsp;—', ' ', filtered)
        if filtered[-1] in ['.', '?', '!']:
            filtered = filtered + '\n'
        text.append(filtered)
    text = text[1:-2]
    text = re.sub(r' +', ' ', ' '.join(text))
    return text
