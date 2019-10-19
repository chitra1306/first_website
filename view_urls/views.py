from django.shortcuts import render
from . import machine_learning_model

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    user_input = request.GET['user_input']
    user_input = machine_learning_model.multiplier(user_input)
    # user_input += " is the test that I entered! "
    return render(request, 'result.html', {'home_input':user_input})
