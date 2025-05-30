# WhatsApp Auto Messenger - README

## 📖 OVERVIEW
This script automatically sends WhatsApp messages at scheduled times or immediately.
It uses image recognition to find and click WhatsApp icon and contacts.

## 🚀 FEATURES
- ⏰ Schedule messages for specific times (24-hour format: HH:MM)
- 🔄 Send multiple messages with customizable repetition
- 👤 Automatically finds and selects target contacts
- 📱 Opens WhatsApp from desktop/taskbar automatically
- 💬 Types and sends messages with realistic typing speed
- ✅ Real-time feedback and progress tracking
- 🛡️ Built-in error handling and validation

## 📋 REQUIREMENTS
1. Python 3.x installed
2. Required Python packages:
   - pyautogui
   - pyfiglet
   - time
   - sys
   - datetime

3. WhatsApp Desktop installed and logged in
4. Two screenshot images (see IMAGE SETUP section)

## 🖼️ IMAGE SETUP (VERY IMPORTANT!)

### Step 1: WhatsApp Icon Screenshot
- Take a screenshot of your WhatsApp icon from the taskbar/desktop
- Make sure the icon is CLEAR and NOT COVERED by other windows
- Crop the image to show ONLY the WhatsApp icon
- Save as: whatsapp.png
- Example: The icon should be visible and clickable (not minimized)

### Step 2: Contact Screenshot  
- Open WhatsApp Desktop
- Go to your contacts/chats list
- Find the target contact you want to message
- Take a screenshot of the contact name/profile picture area
- Make sure the contact is CLEARLY VISIBLE with NO OBSTACLES
- Crop the image to show only the contact area (name + profile pic)
- Save as: contact_target.png

### 📸 SCREENSHOT GUIDELINES:
✅ DO:
- Take clear, high-quality screenshots
- Crop images tightly around the target area
- Ensure good contrast and visibility
- Make sure no other windows are blocking the targets
- Save as PNG format for best quality

❌ DON'T:
- Include unnecessary background elements
- Take blurry or low-quality screenshots
- Leave other windows covering the targets
- Use JPEG format (causes detection issues)

## 📁 FILE STRUCTURE
Your project folder should look like this:
```
Auto Message for Whatsapp/
├── whatsapp_messenger.py
├── README.txt
└── images/
    ├── whatsapp.png          (WhatsApp icon screenshot)
    └── contact_target.png    (Target contact screenshot)
```

## ▶️ HOW TO RUN

1. **Prepare Your Environment:**
   - Close all unnecessary windows
   - Make sure WhatsApp Desktop is closed (script will open it)
   - Ensure your taskbar is visible with WhatsApp icon

2. **Run the Script:**
   ```
   python whatsapp_messenger.py
   ```

3. **Follow the Prompts:**
   - Message: Enter the text you want to send
   - Time: Enter HH:MM (24-hour) or "now" for immediate
   - How many times: Enter number of repetitions

4. **Confirmation:**
   - Review the summary
   - Type 'y' to confirm and start
   - The script will countdown 5 seconds before starting

## 🕐 TIME FORMAT EXAMPLES
- "09:30" = 9:30 AM
- "14:45" = 2:45 PM  
- "23:00" = 11:00 PM
- "now" = Send immediately

## ⚙️ TROUBLESHOOTING

### "WhatsApp icon not found!"
- Check if WhatsApp icon is visible on taskbar/desktop
- Retake the whatsapp.png screenshot
- Make sure no windows are covering the icon
- Try adjusting confidence level in script (0.7 for less strict)

### "Contact not found!"
- Retake the contact_target.png screenshot
- Make sure contact is visible in WhatsApp chat list
- Open WhatsApp manually first to verify contact is there
- Ensure contact name/profile is clearly visible

### "Script not typing/clicking correctly"
- Check if any windows are blocking WhatsApp
- Verify WhatsApp Desktop is the active window
- Make sure your system isn't too slow (increase wait times in script)

## 🔧 CUSTOMIZATION OPTIONS

You can modify these values in the script:
- `confidence=0.8`: Image detection sensitivity (0.7 = less strict, 0.9 = more strict)
- `wait_time=2`: Delay between actions (increase for slower systems)
- `interval=0.05`: Typing speed (increase for slower typing)

## ⚠️ IMPORTANT NOTES

1. **Desktop Environment:** Script works best on Windows with WhatsApp Desktop
2. **Screen Resolution:** Screenshots should match your current screen resolution
3. **WhatsApp State:** Make sure WhatsApp is logged in and ready to use
4. **Rate Limiting:** Built-in 2-second delays between messages to avoid spam detection
5. **Focus Required:** Don't use your computer while script is running for best results

## 🆘 COMMON ISSUES & SOLUTIONS

**Issue:** Script can't find images
**Solution:** Retake screenshots with better quality and proper cropping

**Issue:** WhatsApp doesn't open
**Solution:** Check if WhatsApp Desktop is installed and icon path is correct

**Issue:** Wrong contact selected  
**Solution:** Make sure only target contact is visible in screenshot area

**Issue:** Messages not sending
**Solution:** Verify WhatsApp is active window and message box is accessible

## 📞 SUPPORT
If you're still having issues:
1. Check that all image paths in the script are correct
2. Verify your screenshots match the examples in quality and clarity
3. Test each component separately (WhatsApp opening, contact selection)
4. Make sure your system meets all requirements

## 🎯 TIPS FOR SUCCESS
- Test with "now" option first before scheduling
- Keep screenshots updated if you change themes/layouts
- Start with 1 message to test before multiple repetitions
- Make sure WhatsApp notifications are enabled
- Use the script during stable internet connection

Happy messaging! 🚀