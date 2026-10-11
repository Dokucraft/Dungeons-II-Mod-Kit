import json
import os
import re
import unreal

INTERNAL = os.path.dirname(os.path.abspath(__file__))
SETTINGS = os.path.join(os.path.dirname(INTERNAL), "Settings")
INFO_CLASS = "/Game/Mods/BlueprintLoader/BP_ModInfo"
TRANSLATION_STRUCT = "/Game/Mods/BlueprintLoader/S_ModTranslation"
FIELDS = {"ModName": "name", "Version": "version", "Author": "author", "AuthorUrl": "author_url", "Description": "description", "NexusFileName": "nexus_file_name"}
TRANSLATED = {"ModName": "name", "Description": "description"}
TAG = "ModKitModInfo"
VALID = re.compile(r"^[A-Za-z0-9_-]+$")
MEMBER = re.compile(r"([A-Za-z]+)_\d+_[0-9A-F]{32}(?==)")

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

def quoted(value):
  return '"' + value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'

def read_info():
  path = os.path.join(SETTINGS, "mod_info.json")
  if not os.path.exists(path):
    return {}
  with open(path, encoding="utf-8") as file:
    return json.load(file)

def has_property(target, name):
  try:
    target.get_editor_property(name)
    return True
  except Exception:
    return False

def info_class():
  if assets.does_asset_exist(INFO_CLASS):
    blueprint = assets.load_asset(INFO_CLASS)
  else:
    factory = unreal.BlueprintFactory()
    factory.set_editor_property("parent_class", unreal.PrimaryDataAsset)
    folder, name = INFO_CLASS.rsplit("/", 1)
    blueprint = tools.create_asset(name, folder, unreal.Blueprint, factory)
  defaults = unreal.get_default_object(blueprints.generated_class(blueprint))
  variables = [(field, blueprints.get_basic_type_by_name("string")) for field in FIELDS]
  variables.append(("NexusModsId", blueprints.get_basic_type_by_name("int")))
  variables.append(("Translations", blueprints.get_array_type(blueprints.get_struct_type(assets.load_asset(TRANSLATION_STRUCT)))))
  missing = [(field, kind) for field, kind in variables if not has_property(defaults, field)]
  for field, kind in missing:
    blueprints.add_member_variable(blueprint, field, kind)
  if missing:
    blueprints.compile_blueprint(blueprint)
    assets.save_asset(INFO_CLASS)
  return blueprints.generated_class(blueprint)

def remove_stale(keep):
  for path in assets.list_assets("/Game/Mods", recursive=True):
    asset = path.split(".")[0]
    if asset != keep and assets.get_metadata_tag(assets.load_asset(asset), TAG):
      assets.delete_asset(asset)

def write_translations(info, translations):
  entries = info.get_editor_property("Translations")
  entries.resize(len(translations))
  for index, (language, texts) in enumerate(translations.items()):
    entry = entries[index]
    members = {match.group(1): match.group(0) for match in MEMBER.finditer(entry.export_text())}
    parts = [f"{members['Language']}={quoted(language)}"]
    parts += [f"{members[field]}={quoted(str(texts[key]))}" for field, key in TRANSLATED.items() if texts.get(key)]
    if not entry.import_text("(" + ",".join(parts) + ")"):
      raise RuntimeError(f"Couldn't add the {language} translation from mod_info.json")
    entries[index] = entry
  info.set_editor_property("Translations", entries)

def write_info(name, values, nexus_id, translations):
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
  info.set_editor_property("NexusModsId", nexus_id)
  write_translations(info, translations)
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
write_info(name, values, int(info.get("nexus_mods_id") or 0), info.get("translations") or {})
log(f"{values['name']} {values['version']}")
