# ⛏️ Mine-Script - Auto Miner  
### Created by Evan William

---

## 📜 Description

**Mine-Script** is an intelligent auto-mining bot for Minecraft that uses image detection and simulated keypresses to automate forward mining. It detects **lava danger** in real-time — when spotted, the bot will **retreat** automatically to avoid damage.

Perfect for automating repetitive mining tasks in **single-player** or approved servers.

---

## ⚙️ Requirements

- Python **3.10+**
- Minecraft in **windowed mode** (not fullscreen)
- Required Python packages:
  - `pyautogui`
  - `pyfiglet`

> 💡 Install dependencies:
```bash
pip install pyautogui pyfiglet
````

---

## 📂 Configuration

Before running the script:

### 1. Update image paths in the script:

```python
LAVA_IMAGE = r"path_to_your_lava_image.png"
START_IMAGE = r"path_to_your_start_button_image.png"
```

### 2. Prepare your screenshots:

#### Lava Image:

* Stand near lava in Minecraft.
* Take a screenshot that clearly captures the **lava texture**.
* Crop tightly around the lava and save as `lava.png`.

#### Start Button:

* Use your Minecraft launcher or menu with a visible **Start/Play** button.
* Screenshot and crop only the **Start** button.
* Save as `start_button.png`.

### 3. Set keybindings:

* Make sure `X` is your **mine** key in Minecraft.

---

## 🛠️ How It Works

1. Detects and clicks the **Start Game** button using image recognition.
2. Starts mining by holding `W` (walk forward) and pressing `X` (mine).
3. Mines for the number of **cycles** you specify.
4. If lava is detected on screen, bot **retreats** using the `S` key.
5. Stops automatically when all cycles complete or lava is detected.

---

## ▶️ How To Run

1. Launch Minecraft and go to your mining area.
2. Run the script:

```bash
python mine_script.py
```

3. Enter how many cycles you want the bot to run.
4. Sit back and enjoy automated mining!

> ⛔ Stop anytime with:

* Moving your mouse to the corner of the screen (failsafe)
* Pressing `Ctrl+C` in the terminal

---

## ⛔ Warnings

* **Do NOT use** on multiplayer servers that **prohibit bots or automation**.
* Always use responsibly and ethically.
* This tool is intended for personal use, learning, and experimentation.

---

## 🧠 Pro Tips

* Maintain consistent screen **brightness and resolution**.
* Ensure no overlays (chat, tooltips, or menus) are blocking the lava or button.
* For best results, **do not multitask** while the bot is running.
* Test with a **short cycle** before letting it run longer.