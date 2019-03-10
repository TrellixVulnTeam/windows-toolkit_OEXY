from app.systemUtils import *
from app.menus.mainMenu import runMainMenu
from os import system
# probably import below is required by pyinstaller:
from pyfiglet import Figlet

def main():

	osType = platformName()

	if osType == "windows":
		system('cls')
		runMainMenu()
	else:
		print("Windows Toolkit") # TODO change to nice header and move it to mainMenu.py
		print("You are not running Windows! This program is made for Windows explicitly.")

if __name__ == '__main__':
	main()