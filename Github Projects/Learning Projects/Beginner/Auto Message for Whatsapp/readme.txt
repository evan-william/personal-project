=======================================
    WhatsApp Auto Messenger Bot
         Created by Evan William
=======================================

📜 Description:
WhatsApp Auto Messenger is a smart automation tool that sends WhatsApp messages at your preferred time. Using advanced image recognition, it finds your contacts and sends personalized messages - perfect for birthday wishes, reminders, or staying in touch with friends and family!

⚙️ Requirements:
- Python 3.10+
- Required Python packages:
    - pyautogui
    - pyfiglet
    - datetime
- WhatsApp Desktop installed and logged in
- Clear screenshots of your WhatsApp icon and target contact

📂 Configuration:
Before running the script, you need to:
1. Update these paths in the script:
   - `WHATSAPP_ICON = r"path_to_your_whatsapp_icon.png"`
   - `CONTACT_IMAGE = r"path_to_your_contact_screenshot.png"`
2. Take proper screenshots (see tips below).
3. Make sure WhatsApp Desktop is ready to use.

📸 Taking Perfect Screenshots:
For WhatsApp Icon:
- Find WhatsApp icon on your taskbar or desktop
- Make sure it's clearly visible (not hidden behind other windows)
- Take a screenshot and crop it to show ONLY the WhatsApp icon
- Save as whatsapp.png

For Contact:
- Open WhatsApp Desktop and go to your chats
- Find the person you want to message
- Screenshot their name and profile picture area
- Make sure nothing is blocking or covering the contact
- Crop tightly around the contact area
- Save as contact_target.png

🛠️ How It Works:
1. Finds and clicks your WhatsApp icon to open the app
2. Waits for WhatsApp to fully load
3. Locates your target contact and selects them
4. At your specified time, types and sends your message
5. Repeats the message as many times as you want
6. Gives you real-time updates throughout the process

▶️ How To Run:
1. Make sure WhatsApp Desktop is closed (the script will open it)
2. Clear your desktop - no windows should block WhatsApp icon or contacts
3. Run the script: `python whatsapp_messenger.py`
4. Enter your message when prompted
5. Choose when to send: specific time (like "14:30") or "now"
6. Decide how many times to send the message
7. Confirm and let the magic happen!

🕐 Time Examples:
- "09:30" = 9:30 AM (great for morning greetings!)
- "20:00" = 8:00 PM (perfect for evening check-ins)
- "00:01" = just after midnight (ideal for birthday wishes)
- "now" = send immediately

⛔ Important Notes:
- Use this responsibly - don't spam people!
- Test with 1 message first before sending multiple
- Keep your screenshots updated if you change WhatsApp themes
- Make sure you have permission to message the contact
- The script includes delays to prevent being flagged as spam

🧠 Pro Tips:
For best results:
- Keep your desktop clean when running the script
- Use high-quality PNG screenshots (not blurry JPEG)
- Test during a stable internet connection
- Don't use your computer while the script runs
- Double-check your message before confirming!

💡 Cool Use Cases:
- Schedule birthday messages for friends
- Send daily good morning/night texts
- Remind family about important events
- Share motivational quotes at specific times
- Keep long-distance relationships strong with regular messages

🔧 Troubleshooting:
Can't find WhatsApp icon? → Check if it's visible on taskbar, retake screenshot
Contact not found? → Make sure contact is clearly visible, no chat bubbles blocking
Messages not sending? → Verify WhatsApp is the active window

Happy Messaging! 💬✨

P.S. - Remember, the best messages come from the heart. Use this tool to stay connected, not to replace genuine conversation!
