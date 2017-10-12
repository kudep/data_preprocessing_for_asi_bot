#!/bin/python3
# -*- coding: utf-8 -*-


import progressbar
import collections
import re

__all__ = ['DatasetAssembler']
class DatasetAssembler():
    def __init__(self, list_files):
        self.list_files = list_files
        self.data_lines = None
        self.bar = progressbar.ProgressBar()
        self.context_line_length = None
        self._make_data_lines()
        self.vocab = None

    def _make_data_lines(self):
        self.data_lines = []
        print('Make data lines')
        self.bar.init()
        for srcfile in self.bar(self.list_files):
            with open(srcfile, 'rt') as src:
                for line in src.readlines():
                    self.data_lines.append(line)


    def save_datasets(self, trainfile, labelfile):
        if self.context_line_length is None:
            self.set_datasets_config()

        context = collections.deque([],self.context_line_length)
        trains = self.data_lines[:-1]
        labels = self.data_lines[1:]

        print('Start write into {}'.format(trainfile))
        self.bar.init()
        with open(trainfile, 'wt') as trainf:
            for train in self.bar(trains):
                train = train.split()
                context.extend(train)
                text = " ".join(context)
                text = re.sub(r'\n', ' ', text)
                text = re.sub(r' +', ' ', text)
                trainf.write(text + '\n')

        print('Start write into {}'.format(labelfile))
        self.bar.init()
        with open(labelfile, 'wt') as labelf:
            for label in self.bar(labels):
                text = re.sub(r'\n', ' ', label)
                text = re.sub(r' +', ' ', text)
                labelf.write(text + '\n')



    def set_datasets_config(self, context_line_length = 250):
        self.context_line_length = context_line_length

    def save_vocab(self, vocabfile, tag_list = ["<unk>", "<s>", "</s>"], max_words = None):
        """Process saves vocab into file."""
        self.get_vocab(tag_list, max_words)
        print('Start write into {}'.format(vocabfile))
        with open(vocabfile, 'wt') as vocf:
            for word in self.vocab:
                vocf.write(word + '\n')

    def get_vocab(self, tag_list = ["<unk>", "<s>", "</s>"], max_words = None):
        if self.vocab is None:
            self._make_vocab(tag_list, max_words)
        if (self.tag_list == tag_list) and (self.max_words == max_words):
            pass
        else:
            self._make_vocab(tag_list, max_words)
        return self.vocab


    def _make_vocab(self, tag_list, max_words = None):
        entire_text = " ".join(self.data_lines)
        self.tag_list = tag_list
        self.max_words = max_words
        words = entire_text.split()
        count = collections.Counter(words).most_common(max_words)
        self.vocab = []
        for word, _ in count:
            self.vocab.append(word)
        self._insert_tag_into_vocab(tag_list)


    def _insert_tag_into_vocab(self,tag_list = None):
        """Process inserts addition tags."""
        #tag insert first in list, for example ["<unk>", "<s>", "</s>"]
        if tag_list:
            vocab_without_tag=[]
            for word in self.vocab:
                if word in tag_list:
                    continue
                else:
                    vocab_without_tag.append(word)
            self.vocab= tag_list + vocab_without_tag
