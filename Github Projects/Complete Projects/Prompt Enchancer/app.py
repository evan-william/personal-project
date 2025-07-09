import os
import sys
import json
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from menu import clear_screen, menu, auth_menu
from animation import type_text, dot_generate

class PromptEnhancer:
    def __init__(self):
        self.api_key = None
        self.model = None
        self.config_file = "config.json"
        
    def load_config(self):
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    return config.get('api_key')
        except:
            pass
        return None
    
    def save_config(self, api_key):
        try:
            config = {'api_key': api_key}
            with open(self.config_file, 'w') as f:
                json.dump(config, f)
        except:
            pass
    
    def authenticate(self):
        clear_screen()
        print(auth_menu())
        
        saved_key = self.load_config()
        if saved_key:
            type_text("Found saved API key. Use it? (y/n): ", 30)
            use_saved = input().strip().lower()
            
            if use_saved in ['y', 'yes', '']:
                type_text("Testing saved API key", 50)
                dot_generate("Testing")
                
                if self.test_api_key(saved_key):
                    self.api_key = saved_key
                    type_text("\n✅ Authentication successful!\n", 30)
                    return True
                else:
                    type_text("\n❌ Saved API key is invalid.\n", 30)
        
        while True:
            try:
                type_text("\nEnter your Gemini API key: ", 30)
                api_key = input().strip()
                
                if not api_key:
                    type_text("❌ API key cannot be empty. Please try again.\n", 30)
                    continue
                
                type_text("Testing API key", 50)
                print()
                dot_generate("Verifying")
                
                if self.test_api_key(api_key):
                    self.api_key = api_key

                    type_text("\n✅ API key valid! Save for future use? (y/n): ", 30)
                    save_key = input().strip().lower()
                    
                    if save_key in ['y', 'yes', '']:
                        self.save_config(api_key)
                        type_text("✅ API key saved!\n", 30)
                    else:
                        type_text("✅ API key not saved (will ask again next time)\n", 30)
                    
                    return True
                else:
                    type_text("\n❌ Invalid API key. Please check and try again.\n", 30)
                    
            except KeyboardInterrupt:
                type_text("\n\n👋 Goodbye!\n", 30)
                sys.exit(0)
            except Exception as e:
                type_text(f"\n❌ Error during authentication: {str(e)}\n", 30)
    
    def test_api_key(self, api_key):
        try:
            genai.configure(api_key=api_key)
            model_names = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']
            
            for model_name in model_names:
                try:
                    model = genai.GenerativeModel(model_name)
                    response = model.generate_content("Test")
                    if response.text:
                        return True
                except:
                    continue
            
            return False
            
        except Exception as e:
            print(f"Debug: API test error - {str(e)}")
            return False
    
    def setup_model(self):
        genai.configure(api_key=self.api_key)
        
        safety_settings = {
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        }
        
        model_names = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']
        
        for model_name in model_names:
            try:
                self.model = genai.GenerativeModel(
                    model_name,
                    safety_settings=safety_settings
                )
                test_response = self.model.generate_content("Hi")
                if test_response.text:
                    print(f"Using model: {model_name}")
                    break
            except Exception as e:
                continue
        
        if not self.model:
            raise Exception("No working Gemini model found")
    
    def enhance_prompt(self, simple_prompt):
        enhancement_prompt = f"""
You are an expert prompt engineer. Your task is to take a simple, basic prompt and transform it into a superior, highly detailed, and effective prompt that will produce much better results when used with AI language models.

Original simple prompt: "{simple_prompt}"

Please enhance this prompt by:
1. Adding specific context and background information
2. Defining the desired output format and structure
3. Including relevant examples or scenarios
4. Specifying the tone, style, and approach
5. Adding constraints or guidelines to improve quality
6. Making it more actionable and clear

Return ONLY the enhanced prompt, without any explanations or additional text. The enhanced prompt should be comprehensive, detailed, and significantly more effective than the original.
"""
        
        try:
            response = self.model.generate_content(enhancement_prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error enhancing prompt: {str(e)}"
    
    def main_loop(self):
        clear_screen()
        print(menu())
        
        type_text("🚀 Welcome to Prompt Enhancer!\n", 40)
        type_text("Transform your simple prompts into superior ones!\n\n", 40)
        
        while True:
            try:
                type_text("=" * 60 + "\n", 20)
                type_text("Enter your simple prompt (or 'quit' to exit): ", 30)
                user_input = input().strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    type_text("\n👋 Thank you for using Tik-AI! Goodbye!\n", 30)
                    break
                
                if not user_input:
                    type_text("❌ Please enter a valid prompt.\n", 30)
                    continue
                
                type_text("\n🔄 Enhancing your prompt", 50)
                print()
                dot_generate("Processing")
                
                enhanced_prompt = self.enhance_prompt(user_input)
                
                type_text("\n" + "=" * 60 + "\n", 20)
                type_text("✨ ENHANCED PROMPT:\n", 40)
                type_text("-" * 60 + "\n", 20)
                type_text(enhanced_prompt, 25)
                type_text("\n" + "-" * 60 + "\n", 20)
                
                type_text("\n📋 Enhanced prompt ready to use!\n", 30)
                
            except KeyboardInterrupt:
                type_text("\n\n👋 Goodbye!\n", 30)
                break
            except Exception as e:
                type_text(f"\n❌ An error occurred: {str(e)}\n", 30)
    
    def run(self):
        try:
            if not self.authenticate():
                type_text("❌ Authentication failed. Exiting.\n", 30)
                return
            
            self.setup_model()
            
            type_text("Press Enter to continue...", 30)
            input()
            
            self.main_loop()
            
        except Exception as e:
            type_text(f"❌ Fatal error: {str(e)}\n", 30)
            sys.exit(1)

def main():
    app = PromptEnhancer()
    app.run()

if __name__ == "__main__":
    main()