#!/usr/bin/env python
#coding:utf-8
"""
  Author:   tishion--<tishion@163.com>
  Purpose: 
  Created: 2014-02-04 11:52:19
"""

import os
import sys
from abc import ABCMeta
from abc import abstractmethod


class InterfaceFileProcessor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def process_file(self, file):
        pass

class FileIterator:
    def __init__(self, dir):
        self.dir = dir

    def for_each_file(self, iprocessor):

        self.__traversal_directory(self.dir, iprocessor)
        return

    def __traversal_directory(self, dir, iprocessor):

        if os.path.isdir(dir):
            for item in os.listdir(dir):
                item_path = os.path.join(dir, item)
                if os.path.isdir(item_path):
                    self.__traversal_directory(item_path, iprocessor)
                else:
                    iprocessor.process_file(item_path)
        return


##def main():
##    pass
##
##if __name__ == '__main__':
##    main()