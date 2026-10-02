@echo off
CALL Tools\mod_id.bat
IF %ERRORLEVEL% NEQ 0 exit /b 1

SET "paks="
FOR /F "usebackq delims=" %%G IN ("Tools\user_settings\game_directory.txt") DO IF NOT DEFINED paks (
  IF EXIST "%%G\Dungeons\Content\Paks\global.utoc" SET "paks=%%G\Dungeons\Content\Paks"
  IF NOT DEFINED paks IF EXIST "%%G\Content\Dungeons\Content\Paks\global.utoc" SET "paks=%%G\Content\Dungeons\Content\Paks"
)
IF NOT DEFINED paks (
  echo Couldn't find the game. Add its install folder to Tools\user_settings\game_directory.txt
  exit /b 1
)

SET "outputFolder=%paks%\~mods\%modName%"
IF NOT EXIST "%outputFolder%" MD "%outputFolder%"

Tools\retoc.exe to-zen --version UE5_6 "Dungeons" "%outputFolder%\%modName%_P.utoc"

CALL Tools\pack_mod_info.bat "%outputFolder%\%modName%_P.pak"