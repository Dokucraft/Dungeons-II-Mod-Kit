import os
import runpy

TOOLS = os.path.dirname(os.path.abspath(__file__))

runpy.run_path(os.path.join(TOOLS, "mod_info.py"))
if os.path.isdir(os.path.join(os.path.dirname(TOOLS), "Textures")):
  runpy.run_path(os.path.join(TOOLS, "import_textures.py"))
