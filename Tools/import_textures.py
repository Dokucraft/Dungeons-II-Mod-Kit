import os
import shutil
import sys
import unreal

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import game_files

KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEXTURES = os.path.join(KIT, "Textures")
CONTENT = os.path.join(KIT, "UE5Project", "Content")
TEMP = "ModKitTemp"
EXTENSIONS = [".png", ".tga", ".jpg", ".jpeg", ".bmp", ".exr"]
TAG = "ModKitTexture"

PROPERTIES = ["compression_settings", "srgb", "lod_group", "filter", "address_x", "address_y", "never_stream"]

registry = unreal.AssetRegistryHelpers.get_asset_registry()
assets = unreal.EditorAssetLibrary

def log(message):
  unreal.log_warning(f"Textures: {message}")

def game_path(file):
  path = os.path.relpath(file, TEXTURES).replace(os.sep, "/")
  if path.lower().startswith("dungeons/content/"):
    path = path[17:]
  return os.path.splitext(path)[0]

def find_files():
  files = {}
  for root, _, names in os.walk(TEXTURES):
    for name in names:
      if os.path.splitext(name)[1].lower() in EXTENSIONS:
        file = os.path.join(root, name)
        path = game_path(file)
        if path in files:
          log(f"{path} has more than one image, using {os.path.relpath(files[path], TEXTURES)}")
          continue
        files[path] = file
  return files

def imported_textures():
  found = {}
  filter = unreal.ARFilter(class_paths=[unreal.TopLevelAssetPath("/Script/Engine", "Texture2D")], package_paths=["/Game"], recursive_paths=True)
  for data in registry.get_assets(filter):
    texture = data.get_asset()
    if assets.get_metadata_tag(texture, TAG):
      found[str(data.package_name)[6:]] = texture
  return found

def read_game_settings(paths):
  settings = {}
  if not paths:
    return settings
  paks = game_files.find_paks()
  if not paks:
    log("couldn't find the game, check Tools/user_settings/game_directory.txt. Textures will be imported with default settings")
    return settings
  extracted = game_files.extract(paks, paths, os.path.join(CONTENT, TEMP))
  registry.scan_paths_synchronous(["/Game/" + TEMP], True)
  for path, base in extracted.items():
    texture = assets.load_asset("/Game/" + os.path.relpath(base, CONTENT).replace(os.sep, "/"))
    if isinstance(texture, unreal.Texture2D):
      row = { name: texture.get_editor_property(name) for name in PROPERTIES }
      row["mips"] = game_files.platform_data(open(base + ".uexp", "rb").read())["mips"] > 1
      settings[path] = row
  return settings

def remove_temp():
  if assets.does_directory_exist("/Game/" + TEMP):
    assets.delete_directory("/Game/" + TEMP)
  shutil.rmtree(os.path.join(CONTENT, TEMP), ignore_errors=True)

def import_texture(path, file, settings, stamp):
  task = unreal.AssetImportTask()
  task.filename = file
  task.destination_path = "/Game/" + os.path.dirname(path)
  task.destination_name = os.path.basename(path)
  task.replace_existing = True
  task.automated = True
  task.save = False
  unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
  texture = assets.load_asset("/Game/" + path)
  if not isinstance(texture, unreal.Texture2D):
    log(f"{path} failed to import")
    return False
  if settings:
    properties = { name: settings[name] for name in PROPERTIES }
    properties["mip_gen_settings"] = unreal.TextureMipGenSettings.TMGS_SIMPLE_AVERAGE if settings["mips"] else unreal.TextureMipGenSettings.TMGS_NO_MIPMAPS
    texture.set_editor_properties(properties)
  else:
    log(f"{path} is not a game texture, check the folder and file name. Imported with default settings")
  assets.set_metadata_tag(texture, TAG, stamp)
  assets.save_loaded_asset(texture, False)
  return True

unreal.SystemLibrary.execute_console_command(None, "s.AllowUnversionedContentInEditor 1")
unreal.SystemLibrary.execute_console_command(None, "cook.AllowCookedDataInEditorBuilds 1")
remove_temp()
files = find_files()
existing = imported_textures()
removed = 0
for path in existing:
  if path not in files:
    assets.delete_asset("/Game/" + path)
    removed += 1
changed = {}
unchanged = 0
for path, file in files.items():
  info = os.stat(file)
  stamp = f"{info.st_mtime_ns}:{info.st_size}"
  texture = existing.get(path)
  if texture and assets.get_metadata_tag(texture, TAG) == stamp:
    unchanged += 1
  elif not texture and assets.does_asset_exist("/Game/" + path):
    log(f"{path} already exists in the Unreal project and wasn't made from the Textures folder, delete it there to use this image")
  else:
    changed[path] = stamp
imported = 0
try:
  settings = read_game_settings(list(changed))
  for path, stamp in changed.items():
    if import_texture(path, files[path], settings.get(path), stamp):
      imported += 1
finally:
  remove_temp()
log(f"{imported} imported, {unchanged} unchanged, {removed} removed")
