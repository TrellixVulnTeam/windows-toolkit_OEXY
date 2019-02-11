import json

def displayMenuFromJSON(filePath, key):

	with open(filePath) as f:
		data = json.load(f)

	menuDict = {}

	# map json to dictionary
	for index, each in enumerate(data[key]):
		menuDict[index + 1]= list(each.values())

	# create menu form dictionary
	for i in menuDict:
		extractedValues = menuDict.get(i, "none")
		displayName = extractedValues[0]
		print("{}{} {}".format(i, ".", displayName))
