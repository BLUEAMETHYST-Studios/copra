Write-Host "Deleting application's directory ..."
Remove-Item "$Env:LOCALAPPDATA/copra" -ItemType Directory

Write-Host "Copying application binaries ..."
xcopy.exe /s application "$Env:LOCALAPPDATA\copra"

Write-Host "Reinstallation of copra completed!"