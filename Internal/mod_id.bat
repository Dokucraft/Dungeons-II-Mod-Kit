SET "modName="
FOR /F "usebackq delims=" %%I IN (`powershell -NoProfile -Command "(Get-Content -Raw 'Settings\mod_info.json' | ConvertFrom-Json).id"`) DO SET "modName=%%I"
IF "%modName%"=="" (
  echo Couldn't read the mod id from Settings\mod_info.json
  exit /b 1
)