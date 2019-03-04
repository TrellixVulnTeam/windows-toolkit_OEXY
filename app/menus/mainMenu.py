import sys
from os import system
from app.chocolateyUtils import *
from app.menus.menuUtils import *
from app.cliUtils import *
from app.scriptsUtils import *
from pathlib import Path
#from app.menus.installMenu import runInstallMenu #fix import
from pyfiglet import Figlet


#================ GLOBAL VARIABLES =================

menusFolderPath = Path("./app/menus/")

#================ GLOBAL FUNCTIONS =================

def backToMainMenu():
	runMainMenu()

# Main Menu options are organised as dictionary for the simplicyty of managing entries
# key(number), display name, function name

#============================================
#================ MAIN MENU =================
#============================================

mainMenuOptionsDict = {
	1 : ["Install Programs", "runInstallMenu"],
	2 : ["System Maintenance", "runMaintenanceMenu"],
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

# This function should be called from external function
def runMainMenu():
	system('cls')
	f = Figlet(font='smslant')
	print(f.renderText('Windows Toolkit'))
	displayMainMenu()

	userChoice = input("What do you want to do? x for exit: ")
	if userChoice.isdigit():
		userChoice = int(userChoice)
		goToSubmenu(userChoice)
	elif userChoice == 'x':
		sys.exit()
	else:
		print("Invalid input!")

#============================================
#================ INSTALL MENU ==============
#============================================

def runInstallMenu():

	installJSONpath = menusFolderPath / "installPrograms.json"
	installJSONkey = 'install programs'
	isChocolateyInstalled = checkIfChocolateyIsInstalled()

	if isChocolateyInstalled == 'true':
		system('cls')
		installMenuLogic(installJSONpath, installJSONkey)
		backToMainMenu()
	else:
		print("Installation processes are performed by Chocolatey package manager. It seams that you don't have Chocolatey installed on this computer.")
		print("If you are not familliar with Chocolatey package manager, I recommend to view their website: https://chocolatey.org/about")
		print()
		userChoice = input("Would you like to install Chocolatey? [y / n] : ")
		if (userChoice == 'y') or (userChoice == 'Y'):
			installChocolatey()
			isChocolateyInstalled = checkIfChocolateyIsInstalled()
			if isChocolateyInstalled == 'true':
				input("Chockolatey has been successfully installed! Press any key to continue...")
			else:
				input("Something went wrong during Chockolatey installation, press any key to get back to main menu...")
		elif (userChoice == 'n') or (userChoice == 'N'):
			backToMainMenu()
		else:
			print("Invalid input!")

#====================================================
#================ SYSTEM MAINTENANCE ================
#====================================================

def runMaintenanceMenu():

	# Variables related to System Maintenance 
	systemMentainenceJSONpath = menusFolderPath / "systemMentainence.json"
	systemMentainenceJSONkey = 'system mentainence operation'
	mentainenceScripsPath = Path("./app/resources/mentainenceScripts/")
	scriptKeyName = "script"

	# load JSON file to get script name to run from it
	with open(systemMentainenceJSONpath) as f:
		loadedJSON = json.load(f)

	system('cls')
	displayMaintenanceMenu(systemMentainenceJSONpath, systemMentainenceJSONkey)

	while True:
		userChoice = submenuFooter()
		if userChoice == 'x':
			backToMainMenu()
			break
		elif userChoice.isdigit():
			userChoiceAsInt = int(userChoice)
			scriptIndex = userChoiceAsInt - 1
			runScriptFromJSON(loadedJSON, mentainenceScripsPath, systemMentainenceJSONkey, scriptIndex, scriptKeyName)

def displayMaintenanceMenu(JSONpath, JSONkey):

	systemMentainenceJSONpath = JSONpath
	systemMentainenceJSONkey = JSONkey
	submenuHeader("System Mentainence Menu")
	displayMenuFromJSON(systemMentainenceJSONpath, systemMentainenceJSONkey)