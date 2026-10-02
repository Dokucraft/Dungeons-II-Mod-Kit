import json
import os
import re
import unreal

TOOLS = os.path.dirname(os.path.abspath(__file__))
SETTINGS = os.path.join(TOOLS, "user_settings")
INFO_CLASS = "/Game/Mods/BlueprintLoader/BP_ModInfo"
FIELDS = {"ModName": "name", "Version": "version", "Author": "author", "AuthorUrl": "author_url", "Description": "description"}
TAG = "ModKitModInfo"
VALID = re.compile(r"^[A-Za-z0-9_-]+$")

assets = unreal.EditorAssetLibrary
blueprints = unreal.BlueprintEditorLibrary
tools = unreal.AssetToolsHelpers.get_asset_tools()

def log(message):
  unreal.log_warning(f"Mod info: {message}")

def spaced(name):
  name = re.sub(r"[-_]+", " ", name)
  name = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", name)
  name = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", " ", name)
  return " ".join(name.split())

def read_info():
  path = os.path.join(SETTINGS, "mod_info.json")
  if not os.path.exists(path):
    return {}
  with open(path, encoding="utf-8") as file:
    return json.load(file)

def info_class():
  if not assets.does_asset_exist(INFO_CLASS):
    factory = unreal.BlueprintFactory()
    factory.set_editor_property("parent_class", unreal.PrimaryDataAsset)
    folder, name = INFO_CLASS.rsplit("/", 1)
    blueprint = tools.create_asset(name, folder, unreal.Blueprint, factory)
    for field in FIELDS:
      blueprints.add_member_variable(blueprint, field, blueprints.get_basic_type_by_name("string"))
    blueprints.compile_blueprint(blueprint)
    assets.save_asset(INFO_CLASS)
  return blueprints.generated_class(assets.load_asset(INFO_CLASS))

def remove_stale(keep):
  for path in assets.list_assets("/Game/Mods", recursive=True):
    asset = path.split(".")[0]
    if asset != keep and assets.get_metadata_tag(assets.load_asset(asset), TAG):
      assets.delete_asset(asset)

def write_info(name, values):
  cls = info_class()
  path = f"/Game/Mods/{name}/ModInfo"
  if assets.does_asset_exist(path):
    info = assets.load_asset(path)
  else:
    factory = unreal.DataAssetFactory()
    factory.set_editor_property("data_asset_class", cls)
    info = tools.create_asset("ModInfo", f"/Game/Mods/{name}", cls, factory)
  for field, key in FIELDS.items():
    info.set_editor_property(field, values[key])
  assets.set_metadata_tag(info, TAG, "true")
  assets.save_asset(path)

info = read_info()
name = str(info.get("id") or "")
if not VALID.match(name):
  message = f"The mod id '{name}' in mod_info.json can only contain letters, numbers, - and _"
  unreal.log_error(message)
  raise RuntimeError(message)
values = {key: str(info.get(key) or "") for key in FIELDS.values()}
values["name"] = values["name"] or spaced(name)
remove_stale(f"/Game/Mods/{name}/ModInfo")
write_info(name, values)
log(f"{values['name']} {values['version']}")
