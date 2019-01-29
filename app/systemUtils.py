from sys import platform
#import os.path #TODO: check if this is redundand
import subprocess
import os

def platformName():
	if platform == "win32":
		return "windows"
	else:
		return "other-platform"