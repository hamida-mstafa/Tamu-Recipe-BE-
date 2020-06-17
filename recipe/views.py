from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'Mi ndo ule mse'

    return render(request, 'index.html', {'title': title})