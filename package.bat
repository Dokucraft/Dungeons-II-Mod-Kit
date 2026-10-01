SET /p packageOutput= < Tools\user_settings\package_output.txt
IF /I "%packageOutput:~-5%"==".utoc" SET "packageOutput=%packageOutput:~0,-5%"
IF /I NOT "%packageOutput:~-2%"=="_P" SET "packageOutput=%packageOutput%_P"
SET "packageOutput=%packageOutput%.utoc"

FOR %%F IN ("%packageOutput%") DO (
  SET "outputFolder=%%~dpF"
  SET "packageName=%%~nF"
)
SET "modName=%packageName:~0,-2%"
FOR %%D IN ("%outputFolder%.") DO SET "parentName=%%~nxD"
IF /I NOT "%parentName%"=="%modName%" SET "outputFolder=%outputFolder%%modName%\"
IF NOT EXIST "%outputFolder%" MD "%outputFolder%"
SET "packageOutput=%outputFolder%%packageName%.utoc"

Tools\retoc.exe to-zen --version UE5_6 "Dungeons" "%packageOutput%"