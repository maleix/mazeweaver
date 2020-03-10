# MazeWeaver

## Execute

```bash
pip3 install -r requirements.txt
python3 run_game.py
```

## Start in a concrete level

Mostly for testing purposes, you can start the game in a concrete level

For instance:

```bash
python3 run_game.py --level 4
```

## Make your own labyrinths

Check `levels.py`

## Convert to exe

```powershell
# Must be done in windows
pip3 install pyinstaller
pyinstaller.exe --add-data "resources;resources" run_game.py
```
