from etl import etl
import joblib
from classification_report import classification_report
import json

training = False


etl = etl(training)
data = etl.load()

if training:
	with open('model_config.json') as model_config_file:
		model_config_file = json.load(model_config_file)
	model = model_config_file['models']
	parameters = model_config_file['parameters']

elif not training:
	model = joblib.load('model.sav')
	parameters = None


clr = classification_report(model,parameters,data,training)
clr.report()




