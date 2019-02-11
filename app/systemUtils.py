from sys import platform
import subprocess
import os

def platformName():
	if platform == "win32":
		return "windows"
	else:
		return "other-platform"