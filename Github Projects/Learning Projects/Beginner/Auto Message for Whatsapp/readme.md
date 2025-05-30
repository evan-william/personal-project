# 📩 WhatsApp Auto Messenger Bot  
### Created by Evan William

---

## 📜 Description

**WhatsApp Auto Messenger** is a smart automation tool that sends WhatsApp messages at your preferred time. Using simple image recognition, it finds your contacts and sends personalized messages — perfect for:

- 🎂 Birthday wishes  
- ⏰ Reminders  
- 🤝 Staying in touch with friends and family

---

## ⚙️ Requirements

- Python **3.10+**
- WhatsApp Desktop **installed and logged in**
- Python Packages:
  - `pyautogui`
  - `pyfiglet`
  - `datetime`

> 💡 Install required packages using:
```bash
pip install pyautogui pyfiglet
````

---

## 📂 Configuration

Before running the script, you need to update the following:

### 1. Set the Image Paths in Script

```python
WHATSAPP_ICON = r"path_to_your_whatsapp_icon.png"
CONTACT_IMAGE = r"path_to_your_contact_screenshot.png"
```

### 2. Take Proper Screenshots

#### WhatsApp Icon

* Locate the WhatsApp icon on your desktop or taskbar.
* Make sure it’s clearly visible.
* Crop the screenshot to show **only the icon**.
* Save as `whatsapp.png`.

#### Contact Screenshot

* Open WhatsApp Desktop.
* Go to the chat with your target contact.
* Take a screenshot of their **name and profile picture area**.
* Crop tightly and save as `contact_target.png`.

---

## 🛠️ How It Works

1. Finds and clicks your WhatsApp icon.
2. Waits for WhatsApp to load.
3. Locates and selects your target contact.
4. Sends your message at the scheduled time.
5. Repeats the message as many times as you want.
6. Displays real-time updates in the terminal.

---

## ▶️ How To Run

1. Make sure **WhatsApp Desktop is closed** before starting.
2. Clear your desktop — no windows should block the icon or contact.
3. Run the script:

```bash
python whatsapp_messenger.py
```

4. Follow the prompts:

   * Enter your message
   * Choose when to send (`"now"` or specific time like `"14:30"`)
   * Enter how many times to send the message
5. Confirm and let the magic happen! ✨

---

## 🕐 Time Examples

* `"09:30"` → 9:30 AM (Morning greetings)
* `"20:00"` → 8:00 PM (Evening check-ins)
* `"00:01"` → Just after midnight (Perfect for birthdays)
* `"now"` → Send instantly

---

## ⛔ Important Notes

* Use responsibly — **do not spam**!
* Always test with 1 message first
* Keep screenshots updated if your WhatsApp theme changes
* Ensure you have permission to message the contact
* The script includes delays to mimic human behavior

---

## 🧠 Pro Tips

* Keep your desktop clean when running the bot
* Use **high-quality PNGs**
* Test on a **stable internet connection**
* **Don't touch your mouse/keyboard** while the script runs
* Always double-check your message before confirming

---

## 🧰 Troubleshooting

| Problem                    | Solution                                                          |
| -------------------------- | ----------------------------------------------------------------- |
| ❓ Can't find WhatsApp icon | Ensure it's visible on the taskbar and screenshot is accurate     |
| ❌ Contact not found        | Make sure the name/profile image is not blocked                   |
| 📨 Messages not sending    | Check if WhatsApp is the **active** window and internet is stable |

---
