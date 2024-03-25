import wx  # We need this for working with dialogs and windows

import gui  # We need this for working with dialogs and windows
import globalPluginHandler
from scriptHandler import script

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# Describe the attributes of the script to NVDA.
	@script(
		gesture="kb:nvda+shift+t",  # Configure the key
		description="Run an add-on guide example"  # NVDA input help, may show in Input Gestures
	)
	def script_makeExampleWindow(self, gesture):	# A normal GlobalPlugin script method
		def showExampleWindow():			# Define an internal (nested) function
			gui.messageBox(  # An NVDA function to safely create message dialogs
				# Translators: a message shown to users as an example.
				_(
					"Warning! You are about to do nothing. But you will be doing it with "
					"an important looking dialog window. Continue?"
				), "Example Question Window", wx.OK | wx.CANCEL | wx.ICON_WARNING)
		wx.CallAfter(showExampleWindow)