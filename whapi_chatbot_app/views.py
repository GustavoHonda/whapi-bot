from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests
import json

def health_check(request):
    return JsonResponse({"status": "ok"})

def home(request):
    return render(request, 'whapi_chatbot_app/home.html')

def executar_request(request):
    url = "https://gate.whapi.cloud/messages/text"

    payload = { "typing_time": 0,
                "to": "5511950440023",
                "body": "First message" }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer zNqDoACC4QYwPCIBOjP4Bb7WwA8Jl8h8"
    }
    response_data = None
    if request.method == "POST":
        response = requests.post(url, json=payload, headers=headers)
        print("Status:", response.status_code)
        print("Resposta:", response.json())
        print(response.text)
    response_data = json.dumps(response.json(), indent=4)
    return render(request, 'whapi_chatbot_app/home.html', {'response_data': response_data})
        
