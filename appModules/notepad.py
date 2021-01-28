#A part of notepad_beeper
#
#Copyright (C) 2020-2021, Ty Gillespie. All rights reserved.
#Licensed under the GPL.
#
# Initial code was from the NVDA Developers guide, with some modifications.
# Plans to expand this project are certainly out there.

"""Main appModule."""

import appModuleHandler
import tones
import api
import ui
from scriptHandler import script

class AppModule(appModuleHandler.AppModule):
	def event_gainFocus(self,obj,nextHandler):
		# The focus has been changed, so beep the tone at 500 hz, and for 50 MS.
		tones.beep(500,50)
		nextHandler()

	@script(gesture="kb:NVDA+shift+l")
	def script_sayLineNumber(self,gesture):
		#We're using two nested functioncalls. api.getStatusBarText(obj) and
		#api.getStatusBar(). api.getStatusBar() returns an NVDAObjects.NVDAObject,
		#and api.getStatusBarText(obj) returns the status bar text of
		#the given obj, if it's a status bar.
		#This is how we get the data to split for the line number.
		lineNumList=api.getStatusBarText(api.getStatusBar()).split()
		lineNum=lineNumList[2]+lineNumList[3]
		ui.message(lineNum)
