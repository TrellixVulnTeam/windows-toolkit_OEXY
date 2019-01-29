from app.chocolateyUtils import *
from .mainMenu import runMainMenu #fix import
from os import system

def displayInstallMenu():
	#test v
	print("install menu")

def backToMainMenu():
	runMainMenu()

def runInstallMenu():
	isChocolateyInstalled = checkIfChocolateyIsInstalled()

	if isChocolateyInstalled != 'true':
		system('cls')
		displayInstallMenu()
	else:
		print("Installation processes are performed by Chocolatey package manager. It seams that you don't have Chocolatey installed on this computer.")
		print("If you are not familliar with Chocolatey package manager, I recommend to view their website: https://chocolatey.org/about")
		print()
		print("Would you like to install Chocolatey?")
		userChoice = input("Would you like to install Chocolatey? y / n")
		if (userChoice == 'y') or (userChoice == 'Y'):
			installChocolatey()
		elif (userChoice == 'n') or (userChoice == 'N'):
			backToMainMenu()
		else:
			print("Invalid input!")


