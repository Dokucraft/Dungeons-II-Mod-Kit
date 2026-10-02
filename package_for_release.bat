@echo off
CALL Internal\mod_id.bat
IF %ERRORLEVEL% NEQ 0 exit /b 1

SET "staging=%TEMP%\DungeonsModKitRelease"
IF EXIST "%staging%" RD /S /Q "%staging%"
MD "%staging%\%modName%"

Internal\retoc.exe to-zen --version UE5_6 "Dungeons" "%staging%\%modName%\%modName%_P.utoc"

CALL Internal\pack_mod_info.bat "%staging%\%modName%\%modName%_P.pak"

IF NOT EXIST Release MD Release
IF EXIST "Release\%modName%.zip" DEL "Release\%modName%.zip"
powershell -NoProfile -Command "Add-Type -AssemblyName System.IO.Compression.FileSystem; $zip = [IO.Compression.ZipFile]::Open('%CD%\Release\%modName%.zip', 'Create'); Get-ChildItem '%staging%\%modName%' | ForEach-Object { [void][IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $_.FullName, '%modName%/' + $_.Name, 'Optimal') }; $zip.Dispose()"
RD /S /Q "%staging%"
echo Created Release\%modName%.zip