from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, template_name='index.html')


def about(request):
    return render(request, template_name='about.html')


def events(request):
    return render(request, template_name='events.html')


def eboard(request):
    return render(request, template_name='eboard.html')
