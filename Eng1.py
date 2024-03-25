import globalPluginHandler
from scriptHandler import script
from logHandler import log  # This is what you need for logging
import ui
import api

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	@script(
		description=_("Announces the window class name of the current focus object"),
		gesture="kb:NVDA+leftArrow"
	)
	def script_announceWindowClassName(self, gesture):
		
		navObj = api.getNavigatorObject()
		value = navObj.value
		log.info(type(value))
		# ui.message("val: %s" % (value))
  
  
  