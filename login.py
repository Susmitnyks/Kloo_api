import requests
import json

url = "https://dev.getkloo.com/api/v1/oauth/token"

payload = json.dumps({
  "username": "ajay.shukla+oa@getkloo.com",
  "password": "Jhamar@1515",
  "grant_type": "password",
  "client_id": "96d2d201-a03c-4565-9064-d9df9139eaf0",
  "client_secret": "38W8vJNR3oOIRPiLnDBMRAyyXtIpogOjbQ2KbVjp",
  "scope": "*"
})
headers = {
  'authority': 'dev.getkloo.com',
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9',
  'authorization': 'Bearer null',
  'cache-control': 'no-cache',
  'content-type': 'application/json',
  'cookie': '_ga=GA1.1.1059822648.1698906554; hubspotutk=8260781e9fd0853081811e6dad8b8ca1; messagesUtk=a7631a4b05d9474885288add77aaac2f; _ga_HLH9L1PVBM=GS1.1.1698906554.1.1.1698906622.0.0.0; messagesUtk=a7631a4b05d9474885288add77aaac2f; _clck=1xhi73c%7C2%7Cfha%7C0%7C1433; __hstc=250825561.8260781e9fd0853081811e6dad8b8ca1.1698906555980.1701693776772.1701754612049.3; __hssrc=1; __hssc=250825561.3.1701754612049; _clsk=lpvy4w%7C1701754733590%7C8%7C1%7Cz.clarity.ms%2Fcollect',
  'expires': '0',
  'origin': 'https://dev.getkloo.com',
  'pragma': 'no-cache',
  'referer': 'https://dev.getkloo.com/login',
  'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.json())
print("success now here new feature 1 updated")