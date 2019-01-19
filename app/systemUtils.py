from sys import platform
#import os.path #TODO: check if this is redundand
import subprocess
import os

def platformName():
	if platform == "win32":
		return "windows"
	else:
		return "other-platform"

#TODO make it silent
#@staticmethod
def checkIfChocolateyIsInstalled():
	try:
		subprocess.call(["choco", "--version"])
	except OSError as e:
		if e.errno == os.errno.ENOENT:
			return 'false'
	else:
		return 'true'

def installChocolatey():
	#TODO
	print('installing chocolatey')