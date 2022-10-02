from django.shortcuts import render

def home_page(request):
    return render(request, 'home_page.html')

def new_game(request):
    return render(request, 'new_game.html')

def scorecard(request):
    return render(request, 'scorecard.html')
