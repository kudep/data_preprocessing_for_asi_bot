#!/bin/python3
# -*- coding: utf-8 -*-

import pysrt
from chardet.universaldetector import UniversalDetector

__all__ = ['SubtitleParser']

class SubtitleParser():
    def __init__(self):
        self.detector = UniversalDetector()

    def check_encoding(self, subfilename, encoding = 'utf-8'):
        with open(subfilename, 'rb') as subs:
            self.detector.reset()
            for line in subs.readlines():
                self.detector.feed(line)
                if self.detector.done: break
            self.detector.close()
            return self.detector.result['encoding'] == encoding

    def get_substext(self, subfilename, filter_function_for_subs):
        subs =  pysrt.open(subfilename)
        return filter_function_for_subs(subs)
