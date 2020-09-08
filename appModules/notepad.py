# notepad.py
# A part of notepad_beeper
#
# Copyright (C) 2020, Ty Gillespie. All rights reserved.
# Licensed under the GPL.
#
# Initial code was from the NVDA Developers guide, with some modifications. 
# Plans to expand this project are certainly out there. 
import appModuleHandler
import tones
class AppModule(appModuleHandler.AppModule):
	def event_gainFocus(self, obj, nextHandler):
		# The focus has been changed, so beep the tone at 500 hz, and for 50 MS. 
		tones.beep(500, 50)
		nextHandler()