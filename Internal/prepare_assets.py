import os
import runpy

INTERNAL = os.path.dirname(os.path.abspath(__file__))

runpy.run_path(os.path.join(INTERNAL, "mod_info.py"))
if os.path.isdir(os.path.join(os.path.dirname(INTERNAL), "Textures")):
  runpy.run_path(os.path.join(INTERNAL, "import_textures.py"))
