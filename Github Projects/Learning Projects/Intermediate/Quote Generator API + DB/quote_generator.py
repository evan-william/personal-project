import requests
    
def generate_quote():
    response = requests.get("https://zenquotes.io/api/random", timeout=10)
    response.raise_for_status()                 
    data = response.json()[0]                 
    return data["q"], data["a"]