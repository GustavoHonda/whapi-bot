import requests

url = "https://gate.whapi.cloud/messages/text"

payload = { "typing_time": 0,
            "to": "551150440023",
            "body": "First message" }
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer zNqDoACC4QYwPCIBOjP4Bb7WwA8Jl8h8"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)