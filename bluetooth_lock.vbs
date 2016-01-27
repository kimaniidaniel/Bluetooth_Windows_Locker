Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "C:\temp\scripts\python\bluetooth_lock.bat" & Chr(34), 0
Set WinScriptHost = Nothing