from django.shortcuts import render
from .models import Board

#here home is the view
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})
    
def about(request):
    # do something...
    return render(request, 'about.html')

def about_company(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'about_company.html', {'company_name': 'Simple Complex'})