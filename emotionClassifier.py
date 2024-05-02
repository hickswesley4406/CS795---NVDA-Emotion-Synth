import globalPluginHandler
from scriptHandler import script
from logHandler import log  # This is what you need for logging
import ui
import api

scriptDir = os.path.dirname(os.path.abspath(__file__))
distDir = os.path.join(os.path.dirname(scriptDir), 'dist')
sys.path.append(distDir)

from transformers import pipeline


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	@script(
		description=_("Emotion Classification: Analyze Focused Text"),
		gesture="kb:NVDA+leftArrow"
	)
	def script_announceWindowClassName(self, gesture):
		
		classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)		
  
		navObj = api.getNavigatorObject()
		value = navObj.value
		ui.message(value)

	        scores = classifier(value)
  
		max_score = -float('inf')  # Initialize max_score to negative infinity
		max_label = None
  
		for item in scores[0]:
	             if item['score'] > max_score:
		        max_score = item['score']
		 	max_label = item['label']

		log.info(value)
		log.info("Strongest emotion:", max_label)
