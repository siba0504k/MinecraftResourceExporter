import pathlib
import os
import json
import shutil
from tkinter import filedialog
minecraft_path = pathlib.Path(f"{os.getenv('APPDATA')}/.minecraft/")
if not(minecraft_path.exists()):
    print(".minecraftフォルダを発見できませんでした。\n.minecraftフォルダを選択してください。")
    minecraft_path = pathlib.Path(filedialog.askdirectory())
print("出力するフォルダを選択してください。")
output_path = pathlib.Path(filedialog.askdirectory())
print("利用可能なバージョンは以下の通りです。")
for version in minecraft_path.joinpath("versions").glob("*/*.json"):
    print(version.stem)
use_ver = input("出力したいバージョンを入力してください: ")
with minecraft_path.joinpath(f"versions/{use_ver}/{use_ver}.json").open() as f:
    assert_index_number = json.load(f)["assets"]
    print(assert_index_number)
assert_folder = minecraft_path.joinpath("assets")
print(assert_folder.joinpath(f"indexes/{assert_index_number}.json"))
with assert_folder.joinpath(f"indexes/{assert_index_number}.json").open() as f:
    index_json = json.load(f)
print(index_json)

objects_path = assert_folder.joinpath("objects")
for key, propaty in index_json["objects"].items():
    to_file =output_path.joinpath(key)
    to_file.parent.mkdir(parents=True,exist_ok=True)
    from_fire = pathlib.Path(objects_path.joinpath(propaty["hash"][:2],propaty["hash"]))
    shutil.copyfile(from_fire, to_file)
    print(f"{key}のコピーが完了しました。")

