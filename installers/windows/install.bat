mkdir %LOCALAPPDATA%/copra
xcopy /s application %LOCALAPPDATA%/copra

powershell set-executionpolicy unrestricted
powershell .\script.ps1