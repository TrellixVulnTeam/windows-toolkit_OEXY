import json
import os

def runScriptFromJSON(loadedJSON, scriptLocation, mainKey, index, scriptKey):

	json = loadedJSON
	mKey = mainKey
	_index = index

	jsonDict = {}
	# map json to dictionary
	for index, each in enumerate(json[mKey]):
		jsonDict[index] = list(each.values())

	#test
	#print(jsonDict)

	extractedValues = jsonDict.get(_index, scriptKey)
	scriptToRunName = extractedValues[1]

	#test
	#print(extractedValues)

	#test
	#print(scriptLocation)
	#print(scriptToRunName)
	#print(scriptLocation / scriptToRunName)

	scriptToRunPath = scriptLocation / scriptToRunName
	cmd = "python {}".format(scriptToRunPath) 
	#print(cmd)

	os.system(cmd)
	#os.system("cd")

	#subprocess.call([str(scriptToRunPath.resolve())])
