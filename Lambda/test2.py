import requests

def testFunction(event, context):
    r = requests.get("https://www.google.com")
    if r.status_code == 200:
        return "Success request"