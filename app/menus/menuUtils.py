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

#======================================================
#================ INSTALL MENU RELATED ================
#======================================================

def fuction(filePath, mainKey):

	_filePath = filePath
	_mainKey = mainKey

	def returnMenuDictFromJSON(filePath, mainKey):
		with open(filePath) as f:
			data = json.load(f)
		menuDict = {}
		# map json to dictionary
		for index, each in enumerate(data[mainKey]):
			menuDict[index + 1]= list(each.values())
		return menuDict

	def displayManuWithCheckBoxFromDict(menuDict):
		# create menu form dictionary
		for i in menuDict:
			extractedValues = menuDict.get(i, "none")
			displayName = extractedValues[0]
			description = extractedValues[1]
			command = extractedValues[2]
			installFlag = extractedValues[3]
			displayStatus = " "
			if installFlag == 1:
				displayStatus = "*"
			print("{}{} {}{}{} {} {} {}".format(i, ".", "[", displayStatus, "]", displayName, "-", description))

	def changeCheckState(number, menuDict):
		if number <= len(menuDict):
			extractedValues = menuDict.get(number, "none")
			checkStatus = extractedValues[3]
			if checkStatus == 0:
				extractedValues[3] = 1
			if checkStatus == 1:
				extractedValues[3] = 0
			menuDict.update({number: extractedValues})

	def runInstallOrBackToMainMenu(switch, menuDict):
		if switch == 'r':
			runCheckedFunctions(menuDict)

	def runCheckedFunctions():
		for i in mainDict:
			extractedValues = mainDict.get(i, "none")
			functionName = extractedValues[0]
			checkStatus = extractedValues[2]
			if checkStatus == 1:
				exec(functionName+"()") #run function from chocoUtils.py

#========================= INNER FLOW =========================

	menuObject = returnMenuDictFromJSON(_filePath, _mainKey)
	installOrGetBackToMainMenu = 'r'
	while True:
		displayManuWithCheckBoxFromDict(menuObject)
		userChoice = input("type number to check / uncheck function, type [r] to run selected functions, type [x] to get back to main menu: ")
		if userChoice.isdigit():
			userChoice = int(userChoice)
			changeCheckState(userChoice, menuObject)
		elif userChoice == 'r' or userChoice == 'R':
			installOrGetBackToMainMenu = 'r'
			break
		elif userChoice == 'x' or userChoice == 'X':
			installOrGetBackToMainMenu = 'x'
			break
		else:
			print("Invalid input!")

	runInstallOrBackToMainMenu(installOrGetBackToMainMenu, menuObject)

