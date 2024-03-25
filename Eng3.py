import globalPluginHandler
from scriptHandler import script
from logHandler import log  # This is what you need for logging
from datetime import date

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	@script(
		gesture="kb:nvda+shift+l",  # Configure the key
		description="Run an add-on guide example"  # NVDA input help
	)
	def script_captainsLog(self, gesture):
		today = date.today().strftime("%Y.%m.%d")
		log.info(f"NVDA log. Earth date, {today}.")
		log.warning("These are the add-ons of the screen reader NVDA.")
		log.debugWarning("Its continuing mission. To seek out new opportunities to improve lives!")
		log.debug("To empower users!")
		log.error("and to boldly access software that no screen reader has made accessible before!")