import os
import re
import struct
import subprocess

TOOLS = os.path.dirname(os.path.abspath(__file__))
RETOC = os.path.join(TOOLS, "retoc.exe")
REPAK = os.path.join(TOOLS, "repak.exe")
BATCH = 50

def read_setting(file):
  return open(os.path.join(TOOLS, file)).read().strip()

def aes_key():
  return read_setting(os.path.join("configs", "aes_key.txt"))

def find_paks():
  for game in read_setting(os.path.join("user_settings", "game_directory.txt")).splitlines():
    game = game.strip()
    for paks in [os.path.join(game, "Dungeons", "Content", "Paks"), os.path.join(game, "Content", "Dungeons", "Content", "Paks")]:
      if game and os.path.isdir(paks):
        return paks

def extract(paks, paths, out):
  for i in range(0, len(paths), BATCH):
    filters = []
    for path in paths[i:i + BATCH]:
      filters += ["-f", f"/{os.path.basename(path)}.uasset"]
    subprocess.run([RETOC, "-a", aes_key(), "to-legacy", "--no-shaders", "--no-script-objects"] + filters + [paks, out], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
  content = os.path.join(out, "Dungeons", "Content")
  found = {}
  for root, _, names in os.walk(content):
    for name in names:
      if name.endswith(".uasset"):
        base = os.path.join(root, name[:-7])
        found[os.path.relpath(base, content).replace(os.sep, "/").lower()] = base
  return { path: found[path.lower()] for path in paths if path.lower() in found }

def game_textures(paks, out):
  registry = os.path.join(out, "AssetRegistry.bin")
  with open(registry, "wb") as file:
    subprocess.run([REPAK, "-a", aes_key(), "get", os.path.join(paks, "Dungeons-Windows.pak"), "Dungeons/AssetRegistry.bin"], stdout=file, stderr=subprocess.DEVNULL)
  textures = []
  asset_class = None
  process = subprocess.Popen([RETOC, "asset-registry", registry], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, encoding="utf-8", errors="replace")
  for line in process.stdout:
    line = line.strip()
    if line.startswith("asset_class: "):
      asset_class = line[14:-2]
    elif asset_class == "Texture2D" and line.startswith("package_name: \"/Game/"):
      textures.append(line[21:-2])
  process.wait()
  return textures

def platform_data(uexp):
  match = re.search(rb"PF_[A-Za-z0-9_]+\x00", uexp)
  packed = struct.unpack_from("<I", uexp, match.start() - 8)[0]
  offset = match.end() + (8 if packed & (1 << 30) else 0)
  return { "format": match.group()[:-1].decode(), "mips": struct.unpack_from("<i", uexp, offset + 4)[0], "offset": offset + 8 }
