import json

def runScriptFromJSON(loadedJSON, scriptLocation, mainKey, index, scriptKey):

	json = loadedJSON
	mKey = mainKey

	jsonDict = {}
	# map json to dictionary
	for index, each in enumerate(json[mKey]):
		jsonDict[index + 1]= list(each.values())

	extractedValues = jsonDict.get(index, scriptKey)

	print(extractedValues)
