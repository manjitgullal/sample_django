from django.shortcuts import render
from .models import Board

#here home is the view
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})