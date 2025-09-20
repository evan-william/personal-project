# Prompt Enhancer - Gemini Edition

A terminal-based prompt optimization tool that uses Google's Gemini AI to transform basic prompts into detailed, effective instructions for better AI interactions.

## What It Does

This is a prompt enhancement application I built to learn API integration and improve the quality of AI prompts. The tool takes simple, basic prompts and uses Gemini AI to transform them into comprehensive, well-structured instructions that produce significantly better results when used with ChatGPT and other AI models.

Built this to practice working with AI APIs, understand prompt engineering principles, and create useful developer tools with polished terminal interfaces.

## Features

* Gemini AI API integration for intelligent prompt enhancement
* Automatic API key validation and optional persistence
* Multi-model support with fallback to different Gemini versions
* Beautiful terminal interface with ASCII art and animations
* Typing animation effects for enhanced user experience
* Smart configuration management with JSON file storage
* Error handling for API failures and network issues

## Project Structure

```
prompt-enhancer/
├── main.py          # Main application logic and API integration
├── animation.py     # Typing effects and loading animations
├── menu.py         # ASCII art display and screen clearing
├── config.json     # Auto-generated API key storage
├── requirements.txt # Project dependencies
└── README.md       # This file
```

## Requirements

* Python 3.8+
* Google Gemini API key
* Required packages:
  - google-generativeai
  - pyfiglet

Install dependencies:

```bash
pip install google-generativeai pyfiglet
```

## Setup

1. Obtain a Google Gemini API key from Google AI Studio
2. Ensure all utility files (animation.py, menu.py) are present
3. Run the application and enter your API key when prompted
4. Optionally save the key for future sessions

## How to Run

Start the prompt enhancer:

```bash
python main.py
```

Enter your API key, input a basic prompt, and receive an enhanced version optimized for better AI responses.

## How It Works

The application connects to Google's Gemini AI API and sends prompts through a specialized enhancement pipeline. It automatically tries different Gemini model versions for optimal compatibility and provides detailed, structured prompts that include context, specific instructions, and formatting guidelines.

The enhanced prompts are designed to produce more accurate, comprehensive, and useful responses when used with various AI models.

## What I Learned

* Google Gemini AI API integration and authentication
* JSON configuration file management for persistent settings
* Terminal user interface design with animations and effects
* API error handling and fallback strategies
* Multi-model API compatibility and version management
* Prompt engineering principles and optimization techniques
* Asynchronous programming patterns for API calls

## Sample Enhancement

**Basic Input:** "Write about dogs"

**Enhanced Output:** "Please write a comprehensive, well-structured article about dogs that includes the following elements: an engaging introduction, sections covering breed diversity, behavioral characteristics, care requirements, and the human-dog relationship. Use clear headings, provide specific examples, and maintain an informative yet accessible tone throughout. Aim for 800-1000 words with proper paragraph structure."

## Known Issues

* Requires internet connection for API calls
* API key must be configured manually on first run
* Limited error recovery for API quota limits
* Basic prompt validation without content filtering
* Terminal-only interface without GUI option

## Possible Improvements

Could add:
* Web-based interface for easier access
* Batch prompt enhancement for multiple inputs
* Custom enhancement templates for different use cases
* Prompt effectiveness scoring and analytics
* Integration with popular AI platforms
* Collaborative prompt sharing and rating system
* Advanced customization options for enhancement styles

## Author

**Evan William** - Version 1.0 (2025)

Created this to learn API integration while building a practical tool for improving AI interactions. It helped me understand prompt engineering concepts and how to create polished command-line applications.

This taught me valuable lessons about building developer tools with good user experience.

*Learning project - demonstrates AI API integration and prompt optimization techniques for enhanced AI interactions.*
