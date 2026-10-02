SET "header=%TEMP%\DungeonsModKitHeader"
IF EXIST "%header%" RD /S /Q "%header%"

FOR /D %%M IN (Dungeons\Dungeons\Content\Mods\*) DO IF EXIST "%%M\ModInfo.uasset" (
  MD "%header%\Dungeons\Content\Mods\%%~nxM"
  COPY /Y "%%M\ModInfo.uasset" "%header%\Dungeons\Content\Mods\%%~nxM\ModInfo.uasset" >NUL
)

IF EXIST "%header%" (
  DEL "%~1"
  Internal\repak.exe pack -q --version V11 "%header%" "%~1"
  RD /S /Q "%header%"
)