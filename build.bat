@echo
call .\virtualenvironment\Scripts\activate.bat
pyinstaller --noconfirm --onedir ^
	--workpath ".\output\build" ^
	--distpath ".\output\dist" ^
	--specpath ".\output" ^
	--add-data "..\virtualenvironment\Lib\site-packages\pyfiglet";."\pyfiglet" ^
	--add-data "..\app";."\app" ^
	windows-toolkit.py
pause