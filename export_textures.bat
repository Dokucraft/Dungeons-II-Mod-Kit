SET "python=python"
WHERE py >nul 2>nul && SET "python=py -3"

%python% -m pip install --quiet --disable-pip-version-check numpy pillow texture2ddecoder

%python% Tools\export_textures.py