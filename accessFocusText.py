import globalPluginHandler
from scriptHandler import script
from logHandler import log 
import ui
import api

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	@script(
		description=_("NVDA API Exploration: Access Focused Text"),
		gesture="kb:NVDA+leftArrow"
	)
	def script_announceWindowClassName(self, gesture):	
  
		navObj = api.getNavigatorObject()
		value = navObj.value
		ui.message(value)

		log.info(value)
