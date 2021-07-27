from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'title': 'Главная страница'}
    return render(request, 'main/index.html', context)

def about(request):
    context = {'title': 'Про нас'}
    return render(request, 'main/about.html', context)
