#!/usr/bin/env python
#coding:utf-8
"""
  Author:   tishion--<tishion@163.com>
  Purpose: 
  Created: 2014-02-04 11:54:19
"""

import os
import string
from pefile import pefile
from fileiterator import *


class ImportSymScanner(InterfaceFileProcessor):

    def __init__(self):
        self.__syms = dict()
        self.__result = list()


    def do_check(self, dir):
        self.__result = list()
        if os.path.exists(dir):
            fi = FileIterator(dir)
            fi.for_each_file(self)
        return self.__result

    def dump_result(self, r=None):
        """
        r:
        [
            (
                file1, 
                [
                    (module1, [sym1,sym2,...,symN]), 
                    (module2, [sym1,sym2,...,symN]), 
                        ..., 
                    (moduleN, [sym1,sym2,...,symN])
                ]
            ),
            
            (file2, [(module1, [sym1,sym2,...,symN]), (module2, [sym1,sym2,...,symN]), ..., (moduleN, [sym1,sym2,...,symN])]),
                ......
            (fileN, [(module1, [sym1,sym2,...,symN]), (module2, [sym1,sym2,...,symN]), ..., (moduleN, [sym1,sym2,...,symN])])
        ]
        """
        if r == None:
            r = self.__result
        for result in r:
            print 'File:', result[0]
            for module in result[1]:
                print '\t' + module[0]
                for sym in module[1]:
                    print '\t\t|-' + sym
            print '\r\n'


    def clear_syms(self):
        self.__syms.clear()


    def add_sym(self, module, sym):
        """
        sym:
            (sym1, sym2, ……, symN)
        """
        module = module.lower()
        symbol_set = set(sym)

        if not self.__syms.has_key(module):
            self.__syms[module] = set()

        self.__syms[module] = self.__syms[module] | symbol_set


    def del_sym(self, module, sym):
        """
        sym:
            (sym1, sym2, ……, symN)
        """
        module = module.lower()
        symbol_set = set(sym)

        if not self.__syms.has_key(module):
            return

        self.__syms[module] = self.__syms[module] - symbol_set
        if 0 == len(self.__syms[module]):
            del self.__syms[module]

    def add_syms(self, mod_syms_dict):
        """
        mod_syms_dict:
        {
            module1 : (sym1, sym2, ……, symN),
            module2 : (sym1, sym2, ……, symN),
                ……
            moduleN : (sym1, sym2, ……, symN)
        }
        """
        raise Exception('Method Not Implemented!')

    def del_syms(self, mod_syms_dict):
        """
        mod_syms_dict:
        {
            module1 : (sym1, sym2, ……, symN),
            module2 : (sym1, sym2, ……, symN),
                ……
            moduleN : (sym1, sym2, ……, symN)
        }
        """        
        raise Exception('Method Not Implemented!')

    def process_file(self, file):
        mod_syms = self.__do_inner_check(file)
        if len(mod_syms):
            result = (file, mod_syms)
            self.__result.append(result)

    def __do_inner_check(self, file):
        """
        mod_syms:
        [
            (module1, [sym1,sym2,...,symN]),
            (module2, [sym1,sym2,...,symN]),
                ...
            (moduleN, [sym1,sym2,...,symN])
        ]
        """
        mod_syms = list()
        try:
            pe = pefile.PE(file, fast_load=True)
            parse_dirctories = [
                pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_IMPORT']]
            pe.parse_data_directories(directories=parse_dirctories)

            for entry in pe.DIRECTORY_ENTRY_IMPORT:
                module = entry.dll.lower()
                if self.__syms.has_key(module):
                    import_syms = [elem.name for elem in entry.imports]
                    syms_intersection = [
                        elem for elem in import_syms if elem in self.__syms[module]]
                    if len(syms_intersection):
                        mod_syms_tuple = (module, syms_intersection)
                        mod_syms.append(mod_syms_tuple)
            pe.close()
        except pefile.PEFormatError:
            pass
        except Exception, e:
            print 'File:', file
            print '\tException:', e
            pass

        return mod_syms

def main():
    #dir = r'D:\Program Files (x86)\Tencent\QQIntl'

    #sc = ImportSymScanner()
    #sc.add_sym('msvcr90.dll', ('wcscpy', 'strcpy', 'swprintf'))
    #sc.add_sym('msvcr80.dll', ('wcscpy', 'strcpy', 'swprintf'))
    #sc.add_sym('msvcrt.dll', ('wcscpy', 'strcpy', 'swprintf'))

    #print 'Start...'
    #rl = sc.do_check(dir)
    #print 'Checking is Done!'
    #sc.dump_result(r)
    pass

if __name__ == '__main__':
    main()