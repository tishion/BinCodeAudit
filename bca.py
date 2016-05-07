#!/usr/bin/env python
#coding:utf-8
"""
  Author:   tishion--<tishion@163.com>
  Purpose: 
  Created: 2014/2/9
"""

import os
import sys
import string
from symscan import ImportSymScanner
from reportmaker import ReportMaker

g_str_help =  """
Usage: python bca <target-dir>
    target-dir : target directory path to be scanned.
e.g:
    python bca "c:\window\system32"
"""

def main():
    global g_str_help
    
    if len(sys.argv) <= 1:
        print 'Sytanx Error: missing argument.'
        print g_str_help
        return
        
    target_dir = sys.argv[1]
    
    if not os.path.isdir(target_dir):
        print 'Error: the target-dir:[' + target_dir + '] is not a directory!'
        return

    sc = ImportSymScanner()
    sc.add_sym('ucrtbase.dll', ())
    #sc.add_sym('msvcr90.dll', ('wcscpy', 'strcpy', 'swprintf'))
    #sc.add_sym('msvcr80.dll', ('wcscpy', 'strcpy', 'swprintf'))
    #sc.add_sym('msvcrt.dll', ('wcscpy', 'strcpy', 'swprintf'))
    #sc.add_sym('kernel32.dll', ('lstrcpyA', 'lstrcpyW', 'lstrcatA', 'lstrcatW'))
    #sc.add_sym('shlwapi.dll', ('StrCpyA', 'StrCpyW'))


    print 'Scanning ...'
    rl = sc.do_check(target_dir)
    print 'Scanning is Done!'
    
    rm = ReportMaker()
    print 'Generating report ...'
    rm.GenerateNewReport(target_dir, rl)
    print 'Opening report ...'
    rm.OpenReport()

if __name__ == '__main__':
    main()