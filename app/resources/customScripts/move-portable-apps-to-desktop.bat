echo on
set drive-labell="DANE"
for /f "tokens=1" %%a in (' wmic volume get driveletter^,label ^| find /i %drive-labell%') do set "driveletter=%%a"
set path-to-folder-with-portable-apps=%driveletter%\CLOUD\MEGA\dane\programy\portable
set path-to-user-desktop=%USERPROFILE%\Desktop\
:: switching drives
::%driveletter%
::cd %path-to-folder-with-portable-apps%
::C:
::cd %path-to-user-desktop%
For /R %path-to-folder-with-portable-apps% %%G IN (*.lnk) do copy /V "%%G" %path-to-user-desktop%
pause