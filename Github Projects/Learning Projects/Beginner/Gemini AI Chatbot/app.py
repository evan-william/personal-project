import google.generativeai as genai
import inquirer
import time
import os
import platform
import subprocess
from pyfiglet import Figlet

# Global Variables
api_key = "" # EMPTY START
model_name = "" # EMPTY START (BOTH WILL BE FILLED BY USER!)

# Clear Screen
def clear_screen():
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

# ASCII for First Menu
def ascii_title():
    f = Figlet(font='slant')
    return f.renderText("AI-Chatbot")

# First Menu
def firstmenu():
    return f"""
{ascii_title()}
                    By: Evan William
                    Version: 1.1
                    Currently Supports: Gemini only!
"""

# Help Menu
def outputhelpmenu():
    print("Opening help menu...")
    time.sleep(1)
    clear_screen()
    questions = [
        inquirer.List(
            "choice",
            message="Welcome! What do you need help with?",
            choices=["1. How get Gemini API?", "2. How to choose a model?", "3. Back to main menu"]
        )
    ]
    answer = inquirer.prompt(questions)
    print(f"You selected: {answer['choice']}")
    time.sleep(1)

    if answer["choice"] == "1. How get Gemini API?":
        print("""
        🔑 HOW TO GET GEMINI API KEY:
            1. Go to: https://aistudio.google.com/app/apikey
            2. Login with your Google account.
            3. Click on 'Create API Key', for example: AIzaSyD5CPV-XOnIXBaky-9kUjp7UZj5CLmeAEI.
            4. Copy the key and paste it into this app using option 'Insert Gemini API'.
            NOTE: Keep your key secure and do not share it with others!
            """)
        input("\nPress Enter to return to Help Menu...")
        outputhelpmenu()

    elif answer["choice"] == "2. How to choose a model?":
        print("""
        📘 HOW TO CHOOSE A MODEL:
            1. Make sure you've inserted a valid Gemini API key first.
            2. Select the option 'Choose Available Model' from the main menu.
            3. The app will fetch a list of available text generation models from Gemini.
            4. Choose the model you want to use for chatting.
            
        ✅ TIP: Look for models that support 'generateContent' or 'chat' for better interaction!
                """)
        input("\nPress Enter to return to Help Menu...")
        outputhelpmenu()

    elif answer["choice"] == "3. Back to main menu":
        print("Opening menu...")
        time.sleep(1)
        main()

# Main Function
def main():
    clear_screen()
    print(firstmenu())
    questions = [
        inquirer.List(
            "choice",
            message="Welcome! What do you want to do?",
            choices=["1. Insert Gemini API", "2. Choose Available Model", "3. Start Chat Bot", "4. Help", "5. Exit"],
        )
    ]
    answer = inquirer.prompt(questions)
    print(f"You selected: {answer['choice']}")
    time.sleep(1)

    if answer["choice"] == "1. Insert Gemini API":
        insert_api()
    elif answer["choice"] == "2. Choose Available Model":
        choose_model()
    elif answer["choice"] == "4. Help":
        outputhelpmenu()
    elif answer["choice"] == "3. Start Chat Bot":
        if not api_key or not model_name:
            print("❌ Please insert your API key and choose a model first!") # Nothing Found 
            time.sleep(2)
            main()
        else:
            run_chat()
    else:
        print("Exiting App...")
        time.sleep(1)
        os._exit(0)

# Insert API Key
def insert_api():
    global api_key
    api_key = input("Enter your Gemini API key: ")
    genai.configure(api_key=api_key)
    print("✅ API Key Set!")
    time.sleep(1)
    main()

# Choose Model
def choose_model():
    global model_name
    clear_screen()
    print("📦 Fetching available models...\n")
    if not api_key:
        time.sleep(6)
        print("Took longer than expected...")
        time.sleep(6)
        print("No API key has been found, please set an API key first!")
        time.sleep(2)
        main()

    elif api_key:
        models = genai.list_models()
        choices = []

        for model in models:
            if "generateContent" in model.supported_generation_methods: # Only adds if the model can generate text
                choices.append(model.name)

        if not choices: # NOTHING FOUND 
            print("❌ No valid text models found.")
            time.sleep(2)
            main()

        questions = [
            inquirer.List(
                "selected_model",
                message="Select a model to use:",
                choices=choices,
            )
        ]
        answer = inquirer.prompt(questions)
        model_name = answer["selected_model"]
        print(f"✅ Model '{model_name}' selected!")
        time.sleep(1)
        main()

# Start Chat
def run_chat():
    clear_screen()
    print(f"🤖 Starting Gemini Chatbot with model: {model_name}\n")
    model = genai.GenerativeModel(model_name)  # Set model from chosen model name
    chat = model.start_chat() # Starts session from model 

    print("💬 Type 'exit' to quit.\n")

    while True:
        user_input = input("👤 You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        try:
            response = chat.send_message(user_input) # Process user input then return as reponse
            cleaned_text = response.text.replace("*", "") # Cleans up all "*" that AI created (IMO "*" makes everything ugly, so i have to remove it)
            print(f"🤖 Gemini: {cleaned_text}\n")
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()

    """ 
    NOTES MODEL FOR MYSELF
    model.name
    model.description
    model.supported_generation_methods (like generateContent, etc.)  # MORE FOR TEXT GENERATION

    Generation Methods:
    "generateContent" = for generating general text 
    "generateText" = (older naming)
    "chat" = for conversational use
    "textAndImage" = for multimodal input
    "function_calling" = (if supported)

    GET API HERE: https://aistudio.google.com/app/apikey
    """
