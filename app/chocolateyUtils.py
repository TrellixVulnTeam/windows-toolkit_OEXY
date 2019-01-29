import subprocess
import os
from pathlib import Path

resources_folder = Path("resources")

#TODO make it silent
def checkIfChocolateyIsInstalled():
	try:
		subprocess.call(["choco", "--version"])
	except OSError as e:
		if e.errno == os.errno.ENOENT:
			return 'false'
	else:
		return 'true'

def installChocolatey():
	choco_install_script = resources_folder / "install-chocolatey.bat"
	print('installing chocolatey...')
	subprocess.call([str(choco_install_script.resolve())])


def installChocoPackage():
	#TODO
	pass
