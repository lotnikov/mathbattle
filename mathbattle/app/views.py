from django.shortcuts import render
from django.http import HttpResponse
from .models import Tournament

# Create your views here.

def home(request):
    tournaments = Tournament.objects.all()
    print(tournaments)
    return render(request, 'app/index.html', {'items': tournaments})

def test(request):
    return HttpResponse('<h1>test page</h1>')