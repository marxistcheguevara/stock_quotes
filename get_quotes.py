import requests, ast, json

def get_data():
	r = requests.get("https://ratesjson.fxcm.com/DataDisplayer")
	return ast.literal_eval(r.text[5:-3]) if r.status_code == 200 else {'Rates':[]}

def get_data_as_json():	
	return json.dumps(get_data().get('Rates'))