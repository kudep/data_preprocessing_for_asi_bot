import pandas as pd
from os import path
import re
import progressbar
import datetime
import numpy as np
import random

class regex_patterns():
    std_tokinaze = [
                (r'[\s+]',r' '),
                (r'(\\n)',r' '),
                (r"([\w/'+$\s-]+|[^\w/'+$\s-]+)\s*",r" \1 "),
                (r"([\*\"\'\\\/\|\{\}\[\]\;\:\<\>\,\.\?\*\(\)])",r" \1 "),
                (' +',r' ')]
    tokinaze_for_scipop = [
                (r'[\s+]',r' '),
                (r"([\w/'+$\s-]+|[^\w/'+$\s-]+)\s*",r" \1 "),
                (r"([\*\"\'\\\/\|\{\}\[\]\;\:\,\.\?\*\(\)])",r" \1 "),
                (' +',r' '),
                (r'\< next \>',r'<next>')
                ]



def tokinaze_column(lines,patterns):
    '''
    # Tokinaze useless columns df => df
    column_name = 'TEXT'
    patterns = utils.regex_patterns.std_tokinaze
    tokinazed_dataset = utils.tokinaze_column(dataset, column_name,patterns)
    '''
    for from_regex, to_regex in bar(patterns):
        lines=[re.sub(from_regex, to_regex, line) for line in lines]
    return list(lines)

def tokinaze(input_data):
    '''
    # Tokinaze useless columns df => df
    column_name = 'TEXT'
    patterns = utils.regex_patterns.std_tokinaze
    tokinazed_dataset = utils.tokinaze_column(dataset, column_name,patterns)
    '''
    def splin_tokens(lines,patterns):
        for from_regex, to_regex in patterns:
            lines=[re.sub(from_regex, to_regex, line) for line in lines]
        return list(lines)

    bar = progressbar.ProgressBar()
    bar.init()
    patterns = regex_patterns.tokinaze_for_scipop
    output_data = []
    for chat in bar(input_data):
        output_data.append(splin_tokens(chat, patterns))
    return output_data
