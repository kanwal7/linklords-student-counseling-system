import requests
def get_inspirational_quote():
    try:
        response = requests.get("https://api.quotable.io/random", timeout=5)
        return response.json().get("content", "Stay motivated!")
    except:
        return "Keep trying, even when APIs fail!"
