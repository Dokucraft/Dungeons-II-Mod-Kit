SET "modName="
FOR /F "usebackq delims=" %%I IN (`powershell -NoProfile -Command "(Get-Content -Raw 'Tools\user_settings\mod_info.json' | ConvertFrom-Json).id"`) DO SET "modName=%%I"
IF "%modName%"=="" (
  echo Couldn't read the mod id from Tools\user_settings\mod_info.json
  exit /b 1
)