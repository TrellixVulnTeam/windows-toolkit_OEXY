import sys
from os import system
from app.menus.installMenu import runInstallMenu

# Main Menu options are organised as dictionary for the simplicyty of managing entries
# key(number), display name, function name

mainMenuOptionsDict = {
	1 : ["Install Programs", "displayInstallMenu"],
	2 : ["System Maintenance", "displayMaintenanceMenu"],
	3 : ["Custom Scripts", "displayCustomScriptsMenu"]
} 

def displayMainMenu():
	for i in mainMenuOptionsDict:
		extractedValues = mainMenuOptionsDict.get(i, "none")
		displayName = extractedValues[0]

		print("{}{} {}".format(i, ".", displayName))

def goToSubmenu(number):
	if number <= len(mainMenuOptionsDict):
		extractedValues = mainMenuOptionsDict.get(number, "none")
		functionName = extractedValues[1]
		exec(functionName+"()")

# TODO: change to submenu function
def displayInstallMenu():
	runInstallMenu()

# TODO: change to submenu function
def displayMaintenanceMenu():
	print("System Maintenance")

def displayCustomScriptsMenu():
	print("System Maintenance")

# This function should be called from external function
def runMainMenu():
#Test run
	#while True:

		system('cls')

		displayMainMenu()

		userChoice = input("What do you want to do? x for exit: ")
		if userChoice.isdigit():
			userChoice = int(userChoice)
			goToSubmenu(userChoice)
		elif userChoice == 'x':
			sys.exit()
		else:
			print("Invalid input!")