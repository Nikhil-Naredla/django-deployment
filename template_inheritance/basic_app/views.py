from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def other(request):
    return render(request,'other.html')

def relative_url(request):
    return render(request,'relative_url.html')
