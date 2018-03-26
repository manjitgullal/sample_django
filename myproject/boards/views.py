from django.http import HttpResponse

#here home is the view
def home(request):
    return HttpResponse('Hello, World!')