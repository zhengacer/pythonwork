import json

number = [2, 3, 5, 7, 11, 13]

filenanme = 'number.json'
with open(filename, 'w') as f_obj:
	json.dump(number, f_obj)
	
