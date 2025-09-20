# Mine-Script - Auto Miner

A basic Minecraft mining bot that I made to automate the boring parts of mining. Uses simple image recognition to detect lava and avoid falling into it.

## What This Does

Basically, it makes your character walk forward and mine continuously. If it spots lava on the screen, it backs up automatically so you don't die. I built this because manual mining gets really tedious, especially when you're just looking for materials in straight tunnels.

It's nothing fancy - just holds down movement keys and clicks the mine button while scanning for danger.

## Requirements

- Python 3.10+
- Minecraft (needs to be in windowed mode, not fullscreen)
- These packages:
  - `pyautogui`
  - `pyfiglet`

Install them:
```bash
pip install pyautogui pyfiglet
```

## Setup

You need a couple screenshots first:

### Lava Screenshot
- Go to where there's lava in your world
- Take a screenshot showing the lava texture clearly
- Crop it down to just the lava part
- Save as `lava.png`

### Start Button Screenshot  
- Screenshot your Minecraft launcher or main menu
- Crop just the Start/Play button
- Save as `start_button.png`

### Update the Code
Change these file paths in the script:
```python
LAVA_IMAGE = r"lava.png"
START_IMAGE = r"start_button.png"
```

Also make sure your mine key is set to `X` in Minecraft controls.

## How to Use

1. Open Minecraft in windowed mode
2. Go to your mining spot
3. Run the script:
```bash
python mine_script.py
```
4. Tell it how many cycles to run
5. Let it do its thing

To stop it early:
- Move mouse to screen corner (pyautogui failsafe)
- Press Ctrl+C in terminal

## How It Works

Pretty straightforward:
1. Clicks the start button to get into game
2. Holds W to walk forward
3. Repeatedly presses X to mine
4. Scans screen for lava every few seconds
5. If it finds lava, hits S to back up
6. Stops after your specified cycles or if lava detected

## Important Stuff

**Don't use this on multiplayer servers** - most servers ban automation/bots and you'll get kicked or banned.

This is just for single-player worlds or testing on your own server. It's meant to be a fun experiment, not a serious mining tool.

## Limitations

- Only works in windowed mode
- Image recognition can be flaky
- Doesn't handle complex terrain well
- Won't work if your screen resolution/graphics settings change
- Pretty basic pathfinding (just goes forward)
- Can get stuck on obstacles

## Tips

- Test with just 1-2 cycles first
- Keep your graphics settings consistent
- Don't have chat windows or menus open
- Make sure there's decent lighting in your mining area
- Start in a simple straight tunnel

## Troubleshooting

**Bot doesn't start**: Check if your start button screenshot matches what's on screen

**Doesn't detect lava**: Try taking a clearer lava screenshot with better lighting

**Gets stuck**: It's pretty dumb - clear obstacles from the path first

**Moves weirdly**: Make sure Minecraft is the active window

## Project Files

```
mine_script.py    # Main bot script
lava.png         # Lava detection image
start_button.png # Start button image
```

## Author

**Evan William**  
Version 1.0 (2025)

It's a simple automation experiment - nothing too sophisticated but it saves some time on repetitive mining tasks. 

Definitely has room for improvement, but it works well enough for basic mining. Feel free to modify it or build something better.

---

*For single-player use only. Don't get banned from servers.*
