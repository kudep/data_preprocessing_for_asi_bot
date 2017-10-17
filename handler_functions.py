#!/bin/python3
# -*- coding: utf-8 -*-

import pysrt
import re


__all__ = ['filter_function_ted', 'filter_function_ted_for_split_tokens', 'wikiextractor_handler']

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

def filter_function_ted_for_split_tokens(subs):
    text = []
    for line in subs:
        filtered = re.sub(r'\n', ' ', line.text)
        filtered = re.sub(r'\([^)]*\)', ' ', filtered)
        filtered = re.sub(r'&nbsp;—', ' ', filtered)
        if filtered[-1] in ['.', '?', '!']:
            filtered = filtered + '\n'
        # filtered = re.sub(r"([\w/'+$\s-]+|[^\w/'+$\s-]+)\s*", r"\1 ", filtered)
        filtered = re.sub(r"([\*\"\'\\\/\|\{\}\[\]\;\:\<\>\,\.\!\?\*\(\)\"\«\»\“\”\@\#\%\$\„])", r" \1 ", filtered)
        text.append(filtered)
    text = text[1:-2]
    text = re.sub(r' +', ' ', ' '.join(text))
    return text

def wikiextractor_handler(rawtextlines):
    text = []
    for line in rawtextlines:
        filtered = re.sub(r'\n', ' ', line)
        filtered = re.sub(r'\xa0', ' ', filtered)
        filtered = re.sub(r'\([^)]*\)', ' ', filtered)
        filtered = re.sub(r'\<\/doc\>', ' ', filtered)
        filtered = re.sub(r'\<doc.*\>', ' ', filtered)
        filtered = re.sub(r"([\*\"\'\\\/\|\{\}\[\]\;\:\<\>\,\.\!\?\*\(\)\"\«\»\“\”\@\#\%\$\„])", r" \1 ", filtered)
        text.append(filtered)
    text = text[1:-2]
    text = re.sub(r' +', ' ', ' '.join(text))
    return text
