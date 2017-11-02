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
corentire = join(tgt_dir, 'entire.cor')
manentire = join(tgt_dir, 'entire.man')
cortrain = join(tgt_dir, 'train.cor')
mantrain = join(tgt_dir, 'train.man')
cortest = join(tgt_dir, 'test.cor')
mantest = join(tgt_dir, 'test.man')
cordev_test = join(tgt_dir, 'dev_test.cor')
mandev_test = join(tgt_dir, 'dev_test.man')

data_assemb = dataset_assembler.DatasetAssembler(srcfiles)

data_assemb.save_vocab(corvocabfile)
data_assemb.save_vocab(manvocabfile)
data_assemb.set_datasets_config(context_line_length = 140)
data_assemb.save_datasets(corentire, manentire)

cor_outputfiles = [cortrain, cortest, cordev_test]
man_outputfiles = [mantrain, mantest, mandev_test]
proportions = [0.95, 0.025, 0.025]
data_assemb.save_splited_datasets(corentire, cor_outputfiles, proportions)
data_assemb.save_splited_datasets(manentire, man_outputfiles, proportions)
