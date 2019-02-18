import json

def displayMenuFromJSON(filePath, mainKey):

	with open(filePath) as f:
		data = json.load(f)

	menuDict = {}

	# map json to dictionary
	for index, each in enumerate(data[mainKey]):
		menuDict[index + 1]= list(each.values())

	# create menu form dictionary
	for i in menuDict:
		extractedValues = menuDict.get(i, "none")
		displayName = extractedValues[0]
		print("{}{} {}".format(i, ".", displayName))

def displayMenuFromJSONwithCheckBox(filePath, mainKey):

	with open(filePath) as f:
		data = json.load(f)

	menuDict = {}

	# map json to dictionary
	for index, each in enumerate(data[mainKey]):
		menuDict[index + 1]= list(each.values())

	# create menu form dictionary
	for i in menuDict:
		extractedValues = menuDict.get(i, "none")
		displayName = extractedValues[0]
		description = extractedValues[1]
		command = extractedValues[2]
		installFlag = extractedValues[2]

		displayStatus = " "
		if installFlag == 1:
			displayStatus = "*"

		print("{}{} {}{}{} {} {} {}".format(i, ".", "[", displayStatus, "]", displayName, "-", description))

def displayMenuFromJSONwithSeparatorsAndTick(filePath, mainKey):

	with open(filePath) as f:
		data = json.load(f)

