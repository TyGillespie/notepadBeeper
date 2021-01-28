#A part of notepad_beeper
#
#Copyright (C) 2021, Ty Gillespie. All rights reserved.
#Licensed under the GPL.

import globalPluginHandler
from scriptHandler import script
import subprocess

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	@script(gesture="kb:NVDA+shift+control+n")
	def script_launchNotepad(self,gesture):
		#Launch Notepad.
		subprocess.Popen("notepad.exe")
