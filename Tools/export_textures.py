import os
import struct
import sys
import tempfile
from multiprocessing import Pool

import numpy as np
import texture2ddecoder
from PIL import Image

import game_files

KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT = os.path.join(KIT, "Exported Textures")
SEPARATE_FILE = 0x100
DECODERS = { "PF_DXT1": texture2ddecoder.decode_bc1, "PF_DXT5": texture2ddecoder.decode_bc3, "PF_BC4": texture2ddecoder.decode_bc4, "PF_BC5": texture2ddecoder.decode_bc5, "PF_BC7": texture2ddecoder.decode_bc7 }

def data_resources(uasset):
  for trailing in range(0, 33):
    for count in range(1, 64):
      start = len(uasset) - trailing - count * 44 - 4
      if start < 0:
        break
      if struct.unpack_from("<i", uasset, start)[0] == count:
        rows = []
        for i in range(count):
          _, offset, _, size, _, _, flags = struct.unpack_from("<IqqqqiI", uasset, start + 4 + i * 44)
          rows.append((offset, size, flags))
        if all(0 <= offset < 1 << 40 and 0 < size < 1 << 32 and flags < 1 << 20 for offset, size, flags in rows):
          return rows

def first_mip(base):
  uexp = open(base + ".uexp", "rb").read()
  info = game_files.platform_data(uexp)
  offset = info["offset"]
  start, size, flags = data_resources(open(base + ".uasset", "rb").read())[struct.unpack_from("<i", uexp, offset)[0]]
  offset += 4
  if flags & SEPARATE_FILE:
    with open(base + ".ubulk", "rb") as file:
      file.seek(start)
      data = file.read(size)
  else:
    data = uexp[offset:offset + size]
    offset += size
  width, height = struct.unpack_from("<ii", uexp, offset)
  return info["format"], data, width, height

def decode(format, data, width, height):
  if format == "PF_B8G8R8A8":
    return Image.frombuffer("RGBA", (width, height), data, "raw", "BGRA", 0, 1)
  if format == "PF_G8":
    return Image.frombuffer("L", (width, height), data, "raw", "L", 0, 1)
  block_width, block_height = (width + 3) // 4 * 4, (height + 3) // 4 * 4
  image = Image.frombuffer("RGBA", (block_width, block_height), DECODERS[format](data, block_width, block_height), "raw", "BGRA", 0, 1).crop((0, 0, width, height))
  if format == "PF_BC4":
    return image.getchannel("R")
  if format == "PF_BC5":
    rg = np.asarray(image, dtype=np.float32)[:, :, :2] / 127.5 - 1
    blue = np.sqrt(np.clip(1 - (rg ** 2).sum(axis=2), 0, 1))
    return Image.merge("RGB", (image.getchannel("R"), image.getchannel("G"), Image.fromarray(np.round((blue + 1) * 127.5).astype(np.uint8))))
  return image

def exr_attribute(name, kind, value):
  return name + b"\0" + kind + b"\0" + struct.pack("<i", len(value)) + value

def write_exr(file, data, width, height):
  pixels = np.frombuffer(data, dtype="<f2").reshape(height, width, 4)
  channels = b"".join(name + b"\0" + struct.pack("<iB3xii", 1, 0, 1, 1) for name in [b"A", b"B", b"G", b"R"]) + b"\0"
  box = struct.pack("<iiii", 0, 0, width - 1, height - 1)
  header = struct.pack("<ii", 20000630, 2) + exr_attribute(b"channels", b"chlist", channels) + exr_attribute(b"compression", b"compression", b"\0") + exr_attribute(b"dataWindow", b"box2i", box) + exr_attribute(b"displayWindow", b"box2i", box) + exr_attribute(b"lineOrder", b"lineOrder", b"\0") + exr_attribute(b"pixelAspectRatio", b"float", struct.pack("<f", 1)) + exr_attribute(b"screenWindowCenter", b"v2f", struct.pack("<ff", 0, 0)) + exr_attribute(b"screenWindowWidth", b"float", struct.pack("<f", 1)) + b"\0"
  row_size = width * 8
  first_row = len(header) + height * 8
  with open(file, "wb") as out:
    out.write(header)
    out.write(struct.pack(f"<{height}Q", *[first_row + y * (8 + row_size) for y in range(height)]))
    for y in range(height):
      out.write(struct.pack("<ii", y, row_size) + np.ascontiguousarray(pixels[y][:, [3, 2, 1, 0]].T).tobytes())

def export(path, base):
  format, data, width, height = first_mip(base)
  file = os.path.join(OUTPUT, path)
  os.makedirs(os.path.dirname(file), exist_ok=True)
  if format == "PF_FloatRGBA":
    write_exr(file + ".exr", data, width, height)
  else:
    decode(format, data, width, height).save(file + ".png")

if __name__ == "__main__":
  paks = game_files.find_paks()
  if not paks:
    sys.exit("Couldn't find the game, check Tools/user_settings/game_directory.txt")
  with tempfile.TemporaryDirectory() as temp:
    print("Finding textures...")
    textures = game_files.game_textures(paks, temp)
    print(f"Extracting {len(textures)} textures...")
    extracted = game_files.extract(paks, textures, temp)
    print("Exporting...")
    with Pool() as pool:
      pool.starmap(export, extracted.items(), chunksize=8)
  print(f"Exported {len(extracted)} textures to {OUTPUT}")
