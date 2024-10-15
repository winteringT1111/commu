from django.shortcuts import render,redirect

# Create your views here.

def main_page(request):
    return render(request, "main.html")

def test(request):
    return render(request, "test.html")