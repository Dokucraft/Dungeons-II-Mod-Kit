# Minecraft Dungeons II Mod Kit

This is a set of tools to make it easier to work on mods for Minecraft Dungeons II. The tools will only run on Windows.

## Prerequisites

These need to be installed in order to use the tools:

- Unreal Engine 5.6.1
- Python 3.12 or newer

You can download Unreal Engine for free through the Epic Games Store app, just **make sure to select version 5.6.1**. Using a different version of Unreal Engine will cause all sorts of strange issues.

Python is only needed for the `export_textures.bat` tool. You can install it from [python.org](https://www.python.org/downloads/windows/), or by running this in a terminal:

```
winget install -e --id Python.Python.3.14
```

## Folders

| Folder                  | What it's for |
| ----------------------- | ------------- |
| The root folder         | The tools you run: `cook_assets.bat`, `package.bat`, `package_for_release.bat` and `export_textures.bat`. |
| Settings                | Your settings. See **Setup** below. |
| Tools                   | Extra tools you can use when you need them. |
| Internal                | Files the tools use behind the scenes. You don't need to open or change anything in here. |
| UE5Project              | The Unreal project for your mod's Unreal assets. |
| Textures                | Your replacement textures, if you make any. See **Texture mods** below. |
| Dungeons                | Everything that goes into your mod package. |

## Setup

Edit the files in the `Settings` folder to configure the tools:

| File                    | Description   |
| ----------------------- | ------------- |
| editor_directory.txt    | This contains the path to the folder where the Unreal Editor executables are. If the path doesn't exist, the tools find Unreal Engine 5.6 through the Epic Games Store app instead, so you only need to change this for an install the app doesn't know about. |
| game_directory.txt      | This contains the paths to check for the game's install folder, one per line. The first one that exists is used. The defaults are the Steam and Minecraft Launcher install folders; add yours if the game is installed somewhere else. It's used to export textures, to read the original settings of textures you replace, and to put your mod package in the game's `~mods` folder. |
| mod_info.json           | This contains your mod's id, and the name, version, author and description shown for it in Blueprint Loader's mod menu. See the **Mod Info** section below. |

By default, materials are configured to not be packaged. If you want to change that, or if you want to exclude other Unreal assets from being packaged, you can edit `Settings/copy_cooked_assets.rcj`. To include materials, just remove `M_*.u*` and `MI_*.u*`. To exclude certain files, just add the file names at the bottom, each on their own line. If you remove all of the filters, you need to remove `/XF` as well.

## Mod Info

Every mod package made with the mod kit includes a small info file, so players with [Blueprint Loader](https://www.nexusmods.com/minecraftdungeons2/mods/2) installed can see your mod in its Mods menu, in the game's settings. Without Blueprint Loader the file does nothing, and your mod doesn't need Blueprint Loader to work.

Your mod's details go in `Settings/mod_info.json`:

| Field                  | Description   |
| ---------------------- | ------------- |
| id                     | The mod's id, used to name the mod package and its folder in `~mods`. |
| name                   | The mod's name. |
| version                | The mod's version. |
| author                 | Your name. |
| author_url (optional)  | A link that opens when your name is clicked, like your Nexus Mods profile. |
| description (optional) | A short description of the mod. |
| nexus_mods_id (optional) | The mod's id on Nexus Mods, the number at the end of its page address. Blueprint Loader uses it to tell players when an update is out. Nexus Mods gives your mod its id as soon as you create the page, before you upload any files. |
| nexus_file_name (optional) | Only needed if the mod isn't the main file on its Nexus Mods page. The name of its file in the page's file list, which you type in when uploading. Upload every new version with the same file name. |
| translations (optional) | The mod's name and description in other languages. See below. |

Blueprint Loader compares the mod's `version` with the version of its file on Nexus Mods, so keep the two the same.

### Translations

`translations` shows your mod's name and description in the player's language, following the language picked in the game's settings. Add one entry per language code, with a `name`, a `description` or both:

```json
"translations": {
  "fr": { "name": "Mon Mod", "description": "Une courte description du mod." },
  "de-DE": { "name": "Mein Mod" }
}
```

The game's languages are de-DE, en, en-GB, es-ES, es-MX, fr-CA, fr-FR, it-IT, ja-JP, ko-KR, nl-NL, pl-PL, pt-BR, ru-RU, sv-SE, tr-TR, uk-UA, zh-Hans and zh-Hant. An exact match is used first. Otherwise a translation for the same language is used, so `fr` covers both fr-FR and fr-CA. Anything missing uses your normal text.

The info is added when you run `cook_assets.bat`, so run it again after changing the file.

## Texture mods

Replacing textures doesn't need the Unreal editor to be opened at all:

1. Run `export_textures.bat` to export the game's textures to the `Exported Textures` folder.
2. Make a `Textures` folder in the root folder of the mod kit, next to `cook_assets.bat`. Copy the ones you want to change into it, keeping the same path inside it, and edit them. Don't put them in `UE5Project\Content`, since images there aren't packaged.
3. Run `cook_assets.bat`.
4. Run `package.bat`, then start the game.

The **Textures** section below has the details.

## How to use the tools

For anything other than textures, this guide assumes you're already familiar with the game files and how to extract them.

### Unreal Assets

Any 3D model, texture, and a bunch of other things are *Unreal assets*. These files should be managed using the Unreal editor. You can open the project by opening the `Dungeons.uproject` file in the `UE5Project` folder using the editor.

Unreal assets need to be *cooked* before being packaged.

#### Cooking

Run the `cook_assets.bat` tool to cook the assets and automatically copy them to the `Dungeons` folder, ready to be packaged.

You can exclude certain files by editing `Settings/copy_cooked_assets.rcj`, like mentioned in the **Setup** section above. By default, material files are excluded.

#### Precooked Files

For Unreal assets that are already cooked, for example modified blueprint .uasset files, you can put them in the `Precooked` folder and they will automatically be added when running the `cook_assets.bat` tool. If you don't have a `Precooked` folder, simply make one in the root folder of the mod kit, next to `Dungeons`, `UE5Project`, `package.bat`, etc.

Note that any cooked assets you put directly in the `Dungeons` folder will be deleted when running the `cook_assets.bat` tool because it needs to clean up the old assets before copying the new ones into the folder.

#### Textures

To get the game's textures to edit, run the `export_textures.bat` tool. It exports every texture in the game to an `Exported Textures` folder in the root folder of the mod kit, as `.png` files, or `.exr` for the few HDR textures. The folder structure matches what the `Textures` folder needs, so you can copy the ones you want to change straight across. The first time it runs, it installs the Python packages it needs.

To replace game textures, put your images in a `Textures` folder in the root folder of the mod kit, next to `Dungeons`, `UE5Project`, `package.bat`, etc., using the same folder structure and file names as the game. For example, `Textures\Spicewood\Art\Characters\Player\Equipment\Armor\Wolfclutch_Armor\T_Wolfclutch.png`. Images extracted with their `Dungeons\Content` folders still in the path work too. If you don't have a `Textures` folder, simply make one.

When you run `cook_assets.bat`, every image that is new or has changed is imported into the Unreal project with the same settings as the original game texture, read from your game install. Imported textures are removed from the project again when their image is deleted from the `Textures` folder. Images that don't match a game texture are imported with default settings and a warning.

### Other Files

Anything that isn't an Unreal asset, like the game's loose `.json`, `.locres` and `.ini` files, should be added to the `Dungeons` folder. This folder is what will be turned into the mod package.

`.locres` files hold the game's text and translations. `Tools/Locres Editor.html` opens an online editor for them.

### Packaging

To test your mod, you can run the `package.bat` tool to create the mod package. A mod package is three files with the same name, a `.utoc`, a `.ucas` and a `.pak`, and all three are needed for the mod to load. They're named after your mod's id and go in the game's `~mods` folder, like `~mods\My-Mod\My-Mod_P.utoc`, so you can start the game as soon as it finishes.

To package your mod for release, use the `package_for_release.bat` tool instead. It zips the mod package to `Release\My-Mod.zip`, named after your mod's id, with the files in a `My-Mod` folder inside so players can extract it straight into their `~mods` folder.

### Starting Over

`Tools/clean_up_mod_kit.bat` deletes all of your mod files from the mod kit: the `Dungeons`, `Precooked` and `Textures` folders, and the Unreal project's `Content` folder. It asks you to confirm first, but the files can't be recovered, so make a backup of the mod kit folder if you're unsure.