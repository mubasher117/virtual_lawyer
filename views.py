from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from .models import Chatbot
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'virtual_lawyer/index.html')

def about(request):
    return render(request,'virtual_lawyer/about.html')

@csrf_exempt
def chatbot(request):
    myBot = Chatbot.get_ChatBot()
    botResponse = ''
    if request.method == "POST":
        User = request.POST["talk"]
        botResponse = myBot.get_response(User)
        print(botResponse)
        print("printing bot response***************************************")
    return render(request, 'virtual_lawyer/chatbot.html', {"BotResponse": botResponse})

    # return JsonResponse(data)
    
