import torch
import pandas as pd
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer
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
	def script_echoNavObj(self, gesture):
		
		navObj = api.getNavigatorObject()
		value = navObj.value
  
        model_name = "j-hartmann/emotion-english-distilroberta-base"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        trainer = Trainer(model=model)
  
        # Run Predictions
        predictions = trainer.predict(value)
        
        
		# log.info(type(value))
		ui.message("val: %s" % (value))
  

# Run predictions

     

# Transform predictions to labels
preds = predictions.predictions.argmax(-1)
labels = pd.Series(preds).map(model.config.id2label)
scores = (np.exp(predictions[0])/np.exp(predictions[0]).sum(-1,keepdims=True)).max(1)
     

# scores raw
temp = (np.exp(predictions[0])/np.exp(predictions[0]).sum(-1,keepdims=True))
     

# # work in progress
# # container
# anger = []
# disgust = []
# fear = []
# joy = []
# neutral = []
# sadness = []
# surprise = []

# # extract scores (as many entries as exist in pred_texts)
# for i in range(len(pred_texts)):
#   anger.append(temp[i][0])
#   disgust.append(temp[i][1])
#   fear.append(temp[i][2])
#   joy.append(temp[i][3])
#   neutral.append(temp[i][4])
#   sadness.append(temp[i][5])
#   surprise.append(temp[i][6])