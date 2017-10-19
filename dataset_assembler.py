#!/bin/python3
# -*- coding: utf-8 -*-


import progressbar
import collections
import re
import random

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
        self.data_stories = []
        print('Make data lines')
        self.bar.init()
        for srcfile in self.bar(self.list_files):
            story_lines = []
            with open(srcfile, 'rt') as src:
                for line in src.readlines():
                    self.data_lines.append(line)
                    story_lines.append(line)
            self.data_stories.append(story_lines)


    def save_datasets(self, trainfile, labelfile):
        if self.context_line_length is None:
            self.set_datasets_config()

        with open(trainfile, 'wt') as trainf:
            self.bar.init()
            print('Start write into {}'.format(trainfile))
            for story in self.bar(self.data_stories):
                context = collections.deque([],self.context_line_length)
                trains = story[:-1]

                for train in trains:
                    train = train.split()
                    context.extend(train)
                    text = " ".join(context)
                    text = re.sub(r'\n', ' ', text)
                    text = re.sub(r' +', ' ', text)
                    trainf.write(text + '\n')

        with open(labelfile, 'wt') as labelf:
            print('Start write into {}'.format(labelfile))
            self.bar.init()
            for story in self.bar(self.data_stories):
                labels = story[1:]
                for label in labels:
                    text = re.sub(r'\n', ' ', label)
                    text = re.sub(r' +', ' ', text)
                    text = ' '.join(text.strip().split()[:self.context_line_length])
                    labelf.write(text + '\n')

    def save_splited_datasets(self, srcfile, outputfiles, proportions):
        assert len(outputfiles) == len(proportions), "Lens outputfiles and proportions not equal"
        with open(srcfile, 'rt') as srcdesc:
            corpus = srcdesc.readlines()

        # corpus = random.sample(corpus,len(corpus))
        pr_sum = sum(proportions)
        ranges = [component/pr_sum*len(corpus) for component in proportions]
        print(len(corpus))
        deqindexs = collections.deque([0,0],2)
        for index, rang in enumerate(ranges):
            right_border = deqindexs[1] + rang
            deqindexs.append(right_border)
            print('Start write into {}'.format(outputfiles[index]))
            self.bar.init()
            with open(outputfiles[index], 'wt') as tgtdesc:
                for line in self.bar(corpus[int(deqindexs[0]):int(deqindexs[1])]):
                    tgtdesc.write(line)





    def set_datasets_config(self, context_line_length = 70):
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
