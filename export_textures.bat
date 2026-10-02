@echo off
SET "python=python"
WHERE py >nul 2>nul && SET "python=py -3"

%python% -m pip install --quiet --disable-pip-version-check numpy pillow texture2ddecoder

%python% Internal\export_textures.py