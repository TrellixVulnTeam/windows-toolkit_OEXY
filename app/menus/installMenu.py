from app.systemUtils import *
from os import system

def displayInstallMenu():
	#test v
	print("install menu")

def backToMainMenu():
	pass

def runInstallMenu():

	isChocolateyInstalled = checkIfChocolateyIsInstalled()

	if isChocolateyInstalled == 'true':
		system('cls')
		displayInstallMenu()
	else:
		installChocolatey()


