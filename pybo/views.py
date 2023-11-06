from django.shortcuts import render

app_name = 'pybo'

# Create your views here.
def index(request):
    return render(request, 'pybo/index.html')