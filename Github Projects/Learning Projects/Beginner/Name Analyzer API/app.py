import requests
import time
import sys
import platform
import subprocess

def clear_screen():
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

def dot_generate(word):
    for i in range(4):
                dots = "." * i
                print(f"\r{word}{dots}", end='', flush=True)
                time.sleep(0.5)
    time.sleep(0.5)

def analyze_name(name):
    print(f"\n🔍 Analyzing name: {name}\n")
    dot_generate("Fetching data")
    print()

    age_response = requests.get(f"https://api.agify.io?name={name}")
    age_data = age_response.json()
    print(f"📅 Estimated Age: {age_data.get('age', 'Unknown')} (from {age_data.get('count', 0)} samples)")

    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender_data = gender_response.json()
    print(f"🚻 Likely Gender: {gender_data.get('gender', 'Unknown')} (probability: {gender_data.get('probability', 0)*100:.1f}%)")

    nationalize_response = requests.get(f"https://api.nationalize.io?name={name}")
    nationalize_data = nationalize_response.json()

    print("🌍 Possible Nationalities:")
    for country in nationalize_data.get("country", [])[:3]: 
        country_id = country.get("country_id")
        probability = country.get("probability", 0)
        print(f"   - {country_id} ({probability*100:.1f}%)")

    input("=== Press Enter to Return ===")  

if __name__ == "__main__":
    while True:
        clear_screen()
        print("🔠 Simple Name Analyzer App")
        print("(By: Evan William)")
        user_name = input("\nEnter a first name or 0 to exit: ").strip()
        if user_name != "0":
            analyze_name(user_name)
        elif user_name == "0":
             dot_generate("Exiting")
             time.sleep(0.5)
             sys.exit(0)
        else:
            print("❌ Please enter a valid name.")
