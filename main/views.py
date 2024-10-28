from django.shortcuts import render,redirect
from member.models import Characters,Inventory_magic
from users.models import CharInfo
from store.models import Item_magic
from django.utils import timezone
from datetime import datetime
from django.core.paginator import Paginator
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
    inven = Inventory_magic.objects.filter(user_id=request.user)
    paginator = Paginator(inven, 16)  # 한 페이지에 3개의 아이템

    # 페이지 번호를 가져오기
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # 각 페이지의 아이템 목록을 생성
    pages_items = [paginator.page(i).object_list for i in paginator.page_range]

    return render(request, "class/potion.html", {"page_obj": page_obj, "pages_items": pages_items})