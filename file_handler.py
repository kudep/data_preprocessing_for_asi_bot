#!/bin/python3
# -*- coding: utf-8 -*-

from chardet.universaldetector import UniversalDetector

__all__ = ['FileHandler']

class FileHandler():
    def __init__(self, handler_function):
        self.detector = UniversalDetector()
        self.handler_function = handler_function

    def check_encoding(self, subfilename, encoding = 'utf-8'):
        with open(subfilename, 'rb') as subs:
            self.detector.reset()
            for line in subs.readlines():
                self.detector.feed(line)
                if self.detector.done: break
            self.detector.close()
            return self.detector.result['encoding'] == encoding

    def get_handleredtext(self, filename):
        with open(filename, 'rt') as filedesc:
            return self.handler_function(filedesc)
