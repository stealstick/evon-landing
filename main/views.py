from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/main.html',)
    

def policy(request):
    return render(request, 'rules/privacy.html',)


def term(request):
    return render(request, 'rules/term-service.html',)