#!/bin/python3
# -*- coding: utf-8 -*-

import pysrt
from chardet.universaldetector import UniversalDetector

import subtitle_parser
import handler_functions

import sys
from os import listdir
from os.path import isfile, join

import progressbar

src_dir = sys.argv[1]
tgt_dir = sys.argv[2]
srcfiles = [f for f in listdir(src_dir) if isfile(join(src_dir, f))]
subpars = subtitle_parser.SubtitleParser()
bar = progressbar.ProgressBar()
bar.init()
for srcfile in bar(srcfiles):
    if srcfile[-4:] == '.vtt':
        src = join(src_dir, srcfile)
        if not subpars.check_encoding(src):
            print('Encoding fail in file: {}'.format(src))
            continue
        #Start parsing and writung into target file
        tgt = join(tgt_dir, srcfile[:-4] + '.txt')
        with open(tgt, 'wt') as tgtfile:
            tgtfile.write(subpars.get_substext(src, handler_functions.filter_function_ted_for_split_tokens))
    else:
        print('Postfix fail in file: {}'.format(join(src_dir, srcfile)))
        continue
