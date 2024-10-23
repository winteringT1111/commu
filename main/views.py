from django.shortcuts import render,redirect

# Create your views here.

def main_page(request):
    return render(request, "main.html")

def notice(request):
    return render(request, "notice/notice.html")

def world(request):
    return render(request, "notice/world.html")

def system(request):
    return render(request, "notice/system.html")

def totalsystem(request):
    return render(request, "notice/total_system.html")
