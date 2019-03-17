echo off

:: first check if python is installed
python --version > .\tmp\tmp-python-output.txt
findstr /I "python" .\tmp\tmp-python-output.txt
if %errorlevel% equ 0 goto install-pip

:nopython
echo we have no python
del .\tmp\tmp-python-output.txt
echo make sure pyton is installed and run this script again.
echo press any key
pause
goto end

:install-pip
echo we have python, let's install pip!
python get-pip.py

:check-pip
pip --version > .\tmp\tmp-pip-output.txt
findstr /I "pip" .\tmp\tmp-pip-output.txt
if %errorlevel% equ 0 goto install-pip-packages

:nopip
echo we have python installed, but there is no pip (python package installer) installed!
echo please make sure you have installed pip and try again.
goto end

:install-pip-packages
pip install pyinstaller
pip install --user pipenv
pip install virtualenv
pip install pyfiglet
pip install virtualenv
pip install Django
pip install colorclass
goto end

:end
del .\tmp\tmp-python-output.txt
del .\tmp\tmp-pip-output.txt