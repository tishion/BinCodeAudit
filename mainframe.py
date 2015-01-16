#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<>
  Purpose: 
  Created: 2014/1/25
"""

import win32gui
import win32con
from win32con import *
from pywin.mfc import dialog
from pywin.mfc import window
########################################################################
class MainDialog(dialog.Dialog):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        dialog.Dialog.__init__(self)

        
        
    def OnInitDialog(self):
        
        
        
    
    

#########################################################################
#class MainFrame(object):

    ##----------------------------------------------------------------------    
    #def __init__(self):
        #__hwnd = None
        #__wndClass = None
        #child = None
        #pass

    ##----------------------------------------------------------------------    
    #def Create(self, title):
        #child = dict()
        #self.__wndClass = win32gui.WNDCLASS()
        #self.__wndClass.hbrBackground = win32con.COLOR_BTNFACE + 1
        #self.__wndClass.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)
        #self.__wndClass.hIcon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)
        #self.__wndClass.lpszClassName = "MySimpleWindow"
        #self.__wndClass.lpfnWndProc = self.__wndProc
        
        #wndClassAtom = win32gui.RegisterClass(self.__wndClass)
        #wndStyle = (win32con.WS_CAPTION | 
            #win32con.WS_SYSMENU | 
            #win32con.WS_MINIMIZEBOX |           
            #win32con.WS_OVERLAPPED)
        
        #self.__hwnd = win32gui.CreateWindow(
            #wndClassAtom, 
            #title, 
            #wndStyle, 
            #win32con.CW_USEDEFAULT, 
            #win32con.CW_USEDEFAULT, 
            #320,#win32con.CW_USEDEFAULT, 
            #240,#win32con.CW_USEDEFAULT, 
            #0, 0, 0, None)
        
        #child['OpenButton'] = win32gui.CreateWindow(
            #'Button', 
            #'&Open', 
            #win32con.WS_CHILD | win32con.WS_VISIBLE | win32con.BS_PUSHBUTTON, 
            #20, 
            #20, 
            #30,#win32con.CW_USEDEFAULT, 
            #50,#win32con.CW_USEDEFAULT, 
            #self.__hwnd, 0, 0, None)

    ##----------------------------------------------------------------------
    #def Show(self, mode):
        #win32gui.ShowWindow(self.__hwnd, mode)
        #win32gui.UpdateWindow(self.__hwnd)
        
    ##----------------------------------------------------------------------
    #def __wndProc(self, hwnd, msg, wParam, lParam):
        
        #if msg == win32con.WM_CREATE: 
            #print 'message: WM_CREATE'
            
        #if msg == win32con.WM_SIZE: 
            #print 'message: WM_SIZE'
            
        #if msg == win32con.WM_PAINT: 
            #print 'message: WM_PAINT'
            
        #if msg == win32con.WM_CLOSE: 
            #print 'message: WM_CLOSE'
            
        #if msg == win32con.WM_DESTROY:
            #print 'message: WM_DESTROY'
            #win32gui.PostQuitMessage(0)
            
        #return win32gui.DefWindowProc(hwnd, msg, wParam, lParam)

def main():
    pass
    
    #mainframe = MainFrame()
    #mainframe.Create('TestWindow')
    #mainframe.Show(win32con.SW_NORMAL)
    #win32gui.PumpMessages()

if __name__ == '__main__':
        main()

