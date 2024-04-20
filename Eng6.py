import globalPluginHandler
from scriptHandler import script
from logHandler import log  # This is what you need for logging
import ui
import api
import ctypes
import random

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

        navObj = api.getNavigatorObject()
        value = navObj.value

        sentences = value.split('.')
        sentence_count = len(sentences)
        current_sentence_index = 0

        for i in range(0, sentence_count, 2):
            current_sentences = sentences[i:i+2]
            value = '. '.join(current_sentences)  # Reconstructing two sentences
            log.info(value)

            # Randomly select an emotion
            emotions = ["anger", "disgust", "fear", "joy", "neutral", "sadness", "surprise"]
            emotion = random.choice(emotions)
            log.debug("Selected emotion:", emotion)

            set_speech_rate(emotion)
            set_speech_pitch(emotion)