# A part of notepad_beeper
#
# Copyright (C) 2020-2021, Ty Gillespie. All rights reserved.
# Licensed under the GPL.
#
# Initial code was from the NVDA Developers guide, with some modifications.
# Plans to expand this project are certainly out there.
#
# Change log
#
# 2020.1 (8 September, 2020)
# Added a new command (NVDA plus Shift plus L to speak the current line.
# 2020.2, 22 September, 2020
# Formatted code for pep-8
# Added Control+NVDA+Shift+N to open an untitled Notepad file.

"""Main appModule.
"""

import appModuleHandler
import tones
import api
import ui
from scriptHandler import script
import addonHandler


# Not needed yet but could be useful in the future.
addonHandler.initTranslation()


class AppModule(appModuleHandler.AppModule):
    def event_gainFocus(self, obj, nextHandler):
        # The focus has been changed, so beep the tone at 500 hz, and for 50 MS.
        tones.beep(500, 50)
        nextHandler()

    @script(gesture="kb:NVDA+shift+l")
    def script_sayLineNumber(self, gesture):
        # We're using two nested functioncalls. api.getStatusBarText(obj) and
        # api.getStatusBar(). api.getStatusBar() returns an NVDAObjects.NVDAObject,
        # and api.getStatusBarText(obj) returns the status bar text of
        # the given obj, if it's a status bar.
        # This is how we get the data to split for the line number.
        lineNumList = api.getStatusBarText(api.getStatusBar()).split()
        lineNum = lineNumList[2] + lineNumList[3]
        ui.message(lineNum)

    @script(gesture="kb:NVDA+shift+control+n")
    def script_launchNotepad(self. jesture):
        # Launch Notepad.exe using subprocess.popen.
        subprocess.Popen("notepad.exe", startupinfo=info)