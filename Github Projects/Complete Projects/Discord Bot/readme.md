# Simple Discord Bot Demo

A basic Discord bot built with Python and discord.py to demonstrate fundamental bot development concepts and message handling.

## What It Does

This is a simple Discord bot I created to learn the basics of Discord bot development and API integration. The bot responds to specific text messages, handles both public and private message commands, and demonstrates core bot functionality like event handling and message parsing.

Built this to understand how Discord bots work, practice asynchronous Python programming, and learn about secure token management with environment variables.

## Features

* Responds to specific trigger phrases in chat
* Handles public channel messages and private DM commands
* Command prefix system for private message functionality
* Environment variable integration for secure token storage
* Console logging for debugging and monitoring
* Simple message parsing and response logic

## Project Structure

```
discord-bot-demo/
├── bot.py          # Main bot application
├── .env            # Environment variables (token storage)
└── README.md       # This file
```

## Requirements

* Python 3.8+
* Discord Developer Application and Bot Token
* Required package:
  - discord.py

Install the dependency:

```bash
pip install discord.py
```

## Setup

1. Create a Discord Application and Bot at https://discord.com/developers/applications
2. Copy your bot token
3. Create a `.env` file with your token:
```
DISCORD_TOKEN=your_bot_token_here
```
4. Invite the bot to your server with appropriate permissions

## How to Run

Start the bot:

```bash
python bot.py
```

The bot will connect to Discord and begin responding to messages based on the programmed triggers.

## How It Works

The bot uses discord.py's event-driven architecture to listen for message events. When a message matches specific conditions (trigger words or command prefixes), it processes the input and sends appropriate responses either publicly in the channel or privately via DM.

Environment variables keep the bot token secure and separate from the source code.

## What I Learned

* Discord API integration and bot development basics
* Asynchronous Python programming with async/await
* Event-driven programming patterns
* Secure credential management with environment variables
* Message parsing and command handling logic
* Discord permissions and bot invitation process
* Real-time application debugging and logging

## Current Functionality

* Responds to "halo" with a greeting
* Handles dice roll requests with "lempar dadu dong"
* Processes private commands starting with `?` prefix
* Logs all interactions to console for monitoring
* Maintains connection stability with Discord servers

## Known Issues

* Basic command parsing without advanced argument handling
* Limited error handling for network issues
* Simple response logic without complex features
* No persistent data storage or user management
* Minimal command validation and sanitization

## Possible Improvements

Could add:
* Database integration for user data and settings
* More sophisticated command parsing and help system
* Music playback and voice channel integration
* Moderation tools and admin commands
* Custom server-specific configurations
* Slash command support for modern Discord features
* Better error handling and reconnection logic

## Author

**Evan William** - Version 1.0 (2025)

Created this as my introduction to Discord bot development and asynchronous Python programming. It helped me understand how chat bots work and how to integrate with Discord's API.

This was my first bot project, i do it just for fun.

*Demo project - built for learning Discord bot development fundamentals and API integration.*
