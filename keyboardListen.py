#!/urs/bin/env python 
# -*- coding:utf-8 -*-

import pyHook
import win32gui

"""
该程序需安装pyHook, win32等库。
实现了按下Alt+数字键即可print字符串，并获取光标的位置

"""

def OnKeyboardEvent(event):

	def defineKey(key_value, content):

		if event.Alt == 32 and event.Key == str(key_value):
			screen = win32gui.GetCursorPos()
			print screen
			print content

	defineKey(1,"hello world!") 
	defineKey(2,"this is test!") 
	return True

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()

if __name__ == "__main__":

	import pythoncom
	pythoncom.PumpMessages()