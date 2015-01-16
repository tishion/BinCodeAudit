#!/usr/bin/env python
#coding:utf-8
"""
  Author:   tishion--<tishion@163.com>
  Purpose: 
  Created: 2014-02-04 11:58:19
"""

import os
import time
import webbrowser
from mako.template import Template


########################################################################
class ReportMaker:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        self.__filename = ''
        """Constructor"""
        
    #----------------------------------------------------------------------
    def GenerateNewReport(self, tp, rl):
        """"""
        reprot_t = Template(filename='rt')
        ft = time.strftime('%Y-%m-%d-%H%M%S', time.localtime())
        gt = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        
        r_content = reprot_t.render(
            target_path=tp,
            ge_date= gt,
            result_list=rl)

        file_dir = os.path.join(os.environ["TMP"], 'BinCodeAudit')
        if not os.path.isdir(file_dir):
            try:
                os.mkdir(file_dir)
            except:
                file_dir = os.environ["TMP"]
        
        self.__filename = os.path.join(file_dir, 'Report_' + ft + '.html')
        
        r_file = open(self.__filename, mode='w')
        r_file.write(r_content)
        r_file.close()
            
        #----------------------------------------------------------------------
    def OpenReport(self):
        """"""
        try:
            webbrowser.open_new_tab(self.__filename)
        except Exception, e:
            print 'Failed to open report:', e
                
    
#----------------------------------------------------------------------
def main():
    #reprot_t = Template(filename='rt.htm')
    #print reprot_t.render()
    pass

if __name__ == '__main__':
    main()
    