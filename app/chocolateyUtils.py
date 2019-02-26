import subprocess
import os
from pathlib import Path
from app import admin

resources_folder = Path("app/resources")
choco_install_script = resources_folder / "install-chocolatey.bat"
choco_install_packages_script = resources_folder / "install-chocolatey-packages.bat"

#TODO make it silent
def checkIfChocolateyIsInstalled():
	try:
		subprocess.call(["choco", "--version"])
	except OSError as e:
		if e.errno == os.errno.ENOENT:
			return 'false'
	else:
		return 'true' #should be true, false for test

def installChocolatey():
	print('installing chocolatey...')
	#print(choco_install_script.resolve) # to delete, only for test
	subprocess.call([str(choco_install_script.resolve())])

def installChocoPackages(packagesList):
	#subprocess.call([str(choco_install_packages_script.resolve()), packagesList]) #commented to test newer version below

	if not admin.isUserAdmin():
		admin.runAsAdmin()

	for package in packagesList:
		print(package)
		subprocess.call(["choco", "install", package, "-y"])

	input("type anything")

