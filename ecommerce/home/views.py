from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    first_name = 'John'
    last_name = 'Doe'
    name = {'first_name': first_name, 'last_name': last_name}
    return render(request, 'home/home.html', name)

