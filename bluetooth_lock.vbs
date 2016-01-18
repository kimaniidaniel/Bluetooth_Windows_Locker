Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
'WinScriptHost.Run Chr(34) & "c:\Python27\python.exe C:\temp\scripts\python\bluetooth_lock.py" & Chr(34), 0
WinScriptHost.Run Chr(34) & "C:\temp\scripts\python\bluetooth_lock.bat" & Chr(34), 0
Set WinScriptHost = Nothing