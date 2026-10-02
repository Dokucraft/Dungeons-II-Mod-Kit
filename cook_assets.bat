@echo off
SET "ddp=%~dp0"
SET "ddp=%ddp:~0,-1%"

SET /p editorPath= < Tools\user_settings\editor_directory.txt
IF NOT EXIST "%editorPath%\UnrealEditor-Cmd.exe" FOR /F "usebackq delims=" %%P IN (`powershell -NoProfile -Command "(ConvertFrom-Json (Get-Content (Join-Path $env:ProgramData 'Epic\UnrealEngineLauncher\LauncherInstalled.dat') -Raw)).InstallationList.Where({ $_.AppName -eq 'UE_5.6' }).InstallLocation" 2^>nul`) DO SET "editorPath=%%P\Engine\Binaries\Win64"
IF NOT EXIST "%editorPath%\UnrealEditor-Cmd.exe" (
  echo Couldn't find Unreal Engine 5.6. Make sure it's installed, or if it is, put the path to its Engine\Binaries\Win64 folder in Tools\user_settings\editor_directory.txt
  exit /b 1
)

del /S Dungeons\*.uasset
del /S Dungeons\*.ubulk
del /S Dungeons\*.uexp
del /S Dungeons\*.umap
del /S Dungeons\*.ufont
del /S Dungeons\*.uptnl
del /S Dungeons\*.upipelinecache

"%editorPath%\UnrealEditor-Cmd.exe" "%ddp%\UE5Project\Dungeons.uproject" -run=pythonscript -script="%ddp%\Tools\prepare_assets.py" -unattended -nosplash
IF %ERRORLEVEL% NEQ 0 (
  echo Cooking stopped because of the error above.
  exit /b 1
)

"%editorPath%\UnrealEditor-Cmd.exe" "%ddp%\UE5Project\Dungeons.uproject" -run=cook -targetplatform=Windows -cookall -skipzenstore

robocopy /job:Tools\configs\copy_cooked_assets

robocopy /S Precooked Dungeons