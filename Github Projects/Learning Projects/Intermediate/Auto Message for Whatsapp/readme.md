# WhatsApp Auto Messenger

A simple Python bot that automates WhatsApp messages using image recognition and screen automation.

## What It Does

This script helps you send scheduled WhatsApp messages automatically. I built it to handle birthday messages and reminders without having to remember to send them manually. It uses basic image recognition to find your WhatsApp icon and contacts, then sends messages at whatever time you specify.

Honestly, it's pretty basic but gets the job done for simple automation tasks.

## Requirements

- Python 3.10 or newer
- WhatsApp Desktop (needs to be installed and logged in)
- These Python packages:
  - `pyautogui`
  - `pyfiglet`
  - `datetime` (built-in)

Install the packages:
```bash
pip install pyautogui pyfiglet
```

## Setup

You need to take a couple screenshots first:

### WhatsApp Icon Screenshot
- Find your WhatsApp icon (desktop or taskbar)
- Take a screenshot and crop it to just the icon
- Save it as `whatsapp.png` in your project folder

### Contact Screenshot  
- Open WhatsApp Desktop
- Navigate to the person you want to message
- Screenshot their name/profile picture area in the chat list
- Crop it tight and save as `contact_target.png`

### Update the Script
Change these paths in the code:
```python
WHATSAPP_ICON = r"whatsapp.png"
CONTACT_IMAGE = r"contact_target.png"
```

## How to Use

1. Close WhatsApp Desktop completely
2. Clear your desktop (minimize other windows)
3. Run the script:
```bash
python whatsapp_messenger.py
```
4. Enter your message when prompted
5. Set the time (use "now" for immediate or "14:30" format for scheduled)
6. Choose how many times to send it
7. Don't touch your computer while it runs

## Time Format Examples

- `now` - sends right away
- `09:30` - 9:30 AM
- `23:45` - 11:45 PM
- `00:01` - just after midnight (good for birthday messages)

## How It Works

The bot basically:
1. Clicks your WhatsApp icon using image recognition
2. Waits for WhatsApp to load
3. Finds your target contact in the chat list
4. Clicks on them and sends your message
5. Repeats however many times you specified

It adds random delays to make it look more human-like.

## Things to Watch Out For

- Don't spam people (seriously, be respectful)
- Test with 1 message first before sending multiple
- Keep your screenshots updated if WhatsApp changes appearance
- Make sure you have good internet connection
- The script isn't perfect - sometimes image recognition fails

## Common Issues

**Can't find WhatsApp icon**: Make sure it's visible and your screenshot matches exactly

**Contact not found**: Double-check the contact screenshot and make sure their chat is visible in the list

**Messages not sending**: WhatsApp needs to be the active window, and you need stable internet

## Tips

- Keep your desktop clean when running this
- Use clear, high-quality PNG screenshots
- Don't move your mouse or type while the script is running
- Double-check your message text before hitting enter

## Project Structure

```
whatsapp_messenger.py    # Main script
whatsapp.png            # WhatsApp icon screenshot
contact_target.png      # Contact screenshot
```

## Limitations

This is a pretty simple automation tool. It works for basic use cases but has limitations:
- Only works with WhatsApp Desktop
- Relies on image recognition (can break if UI changes)
- No error recovery if something goes wrong
- Pretty basic compared to proper WhatsApp API solutions

## Author

**Evan William**  
Version 1.0 (2025)

It's a simple test, though I'm sure there are better ways to do this with proper APIs.

If you improve it or find bugs, let me know. Always learning better ways to automate repetitive tasks.

---

*Use responsibly and don't spam peop
