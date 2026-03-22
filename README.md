This is a very WIP repo for a new ALttP APWorld. The code is in worlds/alttpr. Creating .apworlds is currently broken, so this dev repo is the only way to run it.

Instructions:
  1. Clone this repo
  2. Run "git submodule update --init".
  3. Generate player option templates using Launcher.py. This will create an example YAML at "Players/Templates/The Legend of Zelda: A Link to the Past.yaml"
  4. Fill out this YAML and any others you want, and place them in the Players folder.
  5. Either create an AP world as normal, or go to the "worlds/alttpr" directory and run "generate_and_launch.py" as a shortcut, then connect the client to "localhost:38281". Note that this script currently deletes the output folder each time it's run.
