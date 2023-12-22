import requests
import json

url = "https://demo.testfire.net/api/login"

payload = json.dumps({
  "username": "jsmith",
  "password": "demo1234"
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
