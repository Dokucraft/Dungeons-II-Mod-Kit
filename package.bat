SET /p packageOutput= < Tools\user_settings\package_output.txt

Tools\retoc.exe to-zen --version UE5_6 "Dungeons" "%packageOutput%"