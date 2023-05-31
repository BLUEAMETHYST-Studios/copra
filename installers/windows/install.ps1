#requires -version 4.0
#requires -RunAsAdministrator

Write-Host "Creating application's directory ..."
New-Item "$Env:LOCALAPPDATA/copra" -ItemType Directory

Write-Host "Copying application binaries ..."
xcopy.exe /s application "$Env:LOCALAPPDATA\copra"

Write-Host "Adding Path Environment Variable ..."
[Environment]::SetEnvironmentVariable("Path", $Env:PATH + ";" + $Env:LOCALAPPDATA + "/copra", "User")

Write-Host "Installation of copra completed!"

