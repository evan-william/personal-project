=======================================
       Mine-Script - Auto Miner
         Created by Evan William
=======================================

📜 Description:
Mine-Script is an auto-mining bot for Minecraft that uses image detection and keypress simulation. It automatically mines forward unless lava is detected, in which case it retreats.

⚙️ Requirements:
- Python 3.10+
- Required Python packages:
    - pyautogui
    - pyfiglet
- Minecraft in windowed mode (not fullscreen)
- Lava and start game screenshots in your specified path

📂 Configuration:
Before running the script, make sure you:
1. Update these paths in the script:
   - `LAVA_IMAGE = r"path_to_your_lava_image.png"`
   - `START_IMAGE = r"path_to_your_start_button_image.png"`
2. Ensure that the game is visible on the screen.
3. Make sure hotkey `x` is set to mine in Minecraft.

🛠️ How It Works:
1. Detects and clicks the "Start Game" button (based on the image).
2. Moves forward (`W`) and mines (`X`) for the number of cycles you specify.
3. If lava is detected using the lava image, the bot retreats (`S`).
4. Bot stops if lava is found or if it finishes all the cycles.

▶️ How To Run:
1. Open Minecraft and go to your mining location.
2. Run the script.
3. Enter how long (how many cycles) you want the bot to run.
4. Let it run. You can stop it anytime by moving your mouse to the screen corner or pressing Ctrl+C on the terminal.

⛔ Warnings:
- Use responsibly and on single-player or permitted servers only.
- Don't use it on multiplayer servers that prohibit automation—this may violate their rules.

🧠 Tip:
For best results, make sure:
- Lighting and resolution stay consistent.
- No overlay (like chat or tooltips) blocks the lava or start button image.

Happy Mining! ⛏️
