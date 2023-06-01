#requires -version 4.0
#requires -RunAsAdministrator

Write-Host "Deleting application's directory ..."
Remove-Item "$Env:LOCALAPPDATA/copra" -ItemType Directory

Write-Host "Removing Path Environment Variable ..."
$path = [Environment]::GetEnvironmentVariable(
    'PATH',
    'User'
)
$path = ($path.Split(';') | Where-Object { $_ -ne $Env:LOCALAPPDATA + "/copra" }) -join ';'
[Environment]::SetEnvironmentVariable(
    'PATH',
    $path,
    'User'
)

Write-Host "Uninstall of copra completed!"