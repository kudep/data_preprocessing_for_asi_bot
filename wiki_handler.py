#!/bin/python3
# -*- coding: utf-8 -*-




import file_handler
import handler_functions

from os import listdir
from os.path import isfile, join
import os

import progressbar

src_dir = os.environ.get("SRCDIR")
tgt_dir = os.environ.get("TGTDIR")
srcfiles = [ f for f in listdir(src_dir) if isfile(join(src_dir, f))]

filehandler = file_handler.FileHandler(handler_functions.wikiextractor_handler)
bar = progressbar.ProgressBar()
bar.init()
for srcfile in bar(srcfiles):
    src = join(src_dir, srcfile)
    tgt = join(tgt_dir, srcfile)
    with open(tgt, 'wt') as tgtdesc:
        tgtdesc.write(filehandler.get_handleredtext(src))
