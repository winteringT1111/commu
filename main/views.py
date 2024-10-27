from django.shortcuts import render,redirect
from member.models import Characters
from users.models import CharInfo
from django.utils import timezone
from datetime import datetime
from django.http import JsonResponse
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





# 출석
def attendance(request):
    getUser = request.user
    char = CharInfo.objects.get(user=getUser)
    userinfo = Characters.objects.get(charID=char.char_id)
    
    current_hour = timezone.localtime(timezone.now()).hour
        
    if request.method == "POST":
        if 1 <= current_hour < 23   :
            char.galeon = int(char.galeon) + 50
            char.save()
            show_modal = "modal1"
        else:
            show_modal = "modal2"   
        return JsonResponse({'show_modal': show_modal})
    
    context = {'character':userinfo}
    
    return render(request, "class/attendance.html",context)

# 마법의 약
def potion(request):
    getUser = request.user
    return render(request, "class/potion.html")