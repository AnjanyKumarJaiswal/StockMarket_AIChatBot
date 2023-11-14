from django.shortcuts import render
from django.http import HttpResponse 
from chatbot import palm_responses

# Create your views here.
def chatbot(request):
    return render(request,"chatbot.html")
#connecting palm api to django
def palmapi(request):
  """Returns a response from the chatbot."""

  prompt = request.GET.get('prompt')
  palm_api = palm_responses.chatbot(prompt)

  return HttpResponse(palm_api, content_type='text/plain')


