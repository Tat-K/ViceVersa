from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'webapp/index.html')

def reverse(request):
    reversed_text = request.GET['usertext'][::-1]
    context = {
        'reversed_text': reversed_text
    }
    return render(request,'webapp/reverse.html', context=context)
