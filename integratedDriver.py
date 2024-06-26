import globalPluginHandler
from scriptHandler import script
from logHandler import log  # This is what you need for logging
import ui
import api
import ctypes

scriptDir = os.path.dirname(os.path.abspath(__file__))
distDir = os.path.join(os.path.dirname(scriptDir), 'dist')
sys.path.append(distDir)

from transformers import pipeline

# Load the NVDA controller client interface DLL
nvdaControllerClient = ctypes.WinDLL("nvdaControllerClient32.dll")

# Connect to NVDA and initialize the controller
nvdaControllerClient.NVDA_controller_client_initialize()

# Function to set the speech rate (speed) based on emotion
def set_speech_rate(emotion):
    log.debug("Setting speech rate for emotion:", emotion)
    if emotion == "anger":
        nvdaControllerClient.speechSetRate(ctypes.c_int(60))  # Moderate speech rate
    elif emotion == "disgust":
        nvdaControllerClient.speechSetRate(ctypes.c_int(55))  # Slightly slower speech rate
    elif emotion == "fear":
        nvdaControllerClient.speechSetRate(ctypes.c_int(50))  # Slower speech rate
    elif emotion == "joy":
        nvdaControllerClient.speechSetRate(ctypes.c_int(70))  # Faster speech rate
    elif emotion == "neutral":
        nvdaControllerClient.speechSetRate(ctypes.c_int(50))  # Default speech rate
    elif emotion == "sadness":
        nvdaControllerClient.speechSetRate(ctypes.c_int(40))  # Slower speech rate
    elif emotion == "surprise":
        nvdaControllerClient.speechSetRate(ctypes.c_int(65))  # Moderate speech rate

# Function to set the speech pitch based on emotion
def set_speech_pitch(emotion):
    log.debug("Setting speech pitch for emotion:", emotion)
    if emotion == "anger":
        nvdaControllerClient.speechSetPitch(ctypes.c_int(70))  # Higher pitch
    elif emotion == "disgust":
        nvdaControllerClient.speechSetPitch(ctypes.c_int(60))  # Moderate pitch
    elif emotion == "fear":
        nvdaControllerClient.speechSetPitch(ctypes.c_int(50))  # Neutral pitch
    elif emotion == "joy":
        nvdaControllerClient.speechSetPitch(ctypes.c_int(50))  # Neutral pitch
    elif emotion == "neutral":
        nvdaControllerClient.speechSetPitch(ctypes.c_int(50))  # Default pitch
    elif emotion == "sadness":
        nvdaControllerClient.speechSetPitch(ctypes.c_int(30))  # Lower pitch
    elif emotion == "surprise":
        nvdaControllerClient.speechSetPitch(ctypes.c_int(60))  # Moderate pitch

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	@script(
		description=_("Announces the window class name of the current focus object"),
		gesture="kb:NVDA+leftArrow"
	)
	def script_announceWindowClassName(self, gesture):
		
		classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)		
  
		navObj = api.getNavigatorObject()
		value = navObj.value

		scores = classifier(value)
  
		max_score = -float('inf')  # Initialize max_score to negative infinity
		emotion = None
  
		for item in scores[0]:
			if item['score'] > max_score:
				max_score = item['score']
				max_label = item['label']

		log.info(value)
		log.info("Strongest emotion:", emotion)

		set_speech_rate(emotion)
            	set_speech_pitch(emotion)

		ui.message(value)
