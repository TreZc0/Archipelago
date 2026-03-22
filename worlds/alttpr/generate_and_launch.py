# Run the Archipelago commands Generate and Launch.
# Assumes this folder is in Archipelago\worlds\alttpr, and Python 3.13 is installed.
# WARNING: this will wipe the Archipelago\output folder
# TODO: Don't wipe the output folder
import os
import shutil
import subprocess
import zipfile


if not os.path.basename(os.getcwd()) == "alttpr":
    print("This script must be run from within the 'alttpr' folder.")
    exit()
os.chdir(os.path.join("..", ".."))
if os.path.exists("output"):
    shutil.rmtree("output")
os.mkdir("output")

subprocess.run(["py", "-3.13", "Generate.py"])
output_zip_filename = os.listdir("output")[0]
output_zip = zipfile.ZipFile(os.path.join("output", output_zip_filename))
output_zip.extractall("output")
rom = None
for filename in os.listdir("output"):
    if filename.endswith(".apalttpr"):
        rom = filename
        break

if not rom:
    print("Error: Could not find the rom file")
    exit()
multiserver = subprocess.Popen(["py", "-3.13", "MultiServer.py", os.path.join("output", output_zip_filename)])
subprocess.run(["py", "-3.13", "Launcher.py", os.path.join("output", rom)])
multiserver.kill()