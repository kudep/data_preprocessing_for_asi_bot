#!/bin/python3
# -*- coding: utf-8 -*-

import pysrt
from chardet.universaldetector import UniversalDetector

import subtitle_parser
import filter_function_for_youtube_subs
import sys

print(sys.argv[1])
sp = subtitle_parser.SubtitleParser()
print(sp.check_encoding(sys.argv[1]))
print(sp.get_substext(sys.argv[1], filter_function_for_youtube_subs.filter_function_ted))
