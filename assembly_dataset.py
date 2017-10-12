#!/bin/python3
# -*- coding: utf-8 -*-




import dataset_assembler

from os import listdir
from os.path import isfile, join
import os

src_dir = os.environ.get("SRCDIR")
tgt_dir = os.environ.get("TGTDIR")
srcfiles = [ join(src_dir, f) for f in listdir(src_dir) if isfile(join(src_dir, f))]


corvocabfile = join(tgt_dir, 'vocab.cor')
manvocabfile = join(tgt_dir, 'vocab.man')
corfile = join(tgt_dir, 'train.cor')
manfile = join(tgt_dir, 'train.man')

data_assemb = dataset_assembler.DatasetAssembler(srcfiles)

data_assemb.save_vocab(corvocabfile)
data_assemb.save_vocab(manvocabfile)
data_assemb.save_datasets(corfile,manfile)
