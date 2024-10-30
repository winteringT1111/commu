from django.shortcuts import render,redirect
from member.models import Characters,Inventory_magic
from users.models import CharInfo
from store.models import Item_magic
from django.utils import timezone
from datetime import datetime
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
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
@login_required(login_url='/')
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


    
# 수업 페이지
def class_main(request):
    return render(request, "class/class_main.html")



# 마법의 약
@login_required(login_url='/')
def potion(request):
    inven = Inventory_magic.objects.filter(user_id=request.user)
    paginator = Paginator(inven, 16)  # 한 페이지에 3개의 아이템

    # 페이지 번호를 가져오기
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    # 각 페이지의 아이템 목록을 생성
    pages_items = [paginator.page(i).object_list for i in paginator.page_range]

    return render(request, "class/potion.html", {"page_obj": page_obj, "pages_items": pages_items})


@login_required(login_url='/')
@require_POST
def check_combination(request):
    try:
        data = json.loads(request.body)
        selected_items = data.get('selected_items', [])

        if set(selected_items) == {"정어리", "밀가루", "버터", "설탕"}:
            result = "success"
            image = "img/test_item/정어리 파이.png"
        else:
            result = "failure"
            image = "img/test_item/빈 물약(꽝).png"
            
        char = CharInfo.objects.get(user=request.user)
        char.classToken -= 1
        char.save()

        return JsonResponse({'result': result, 'image': f"{image}"})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)


# 약초학
def herb(request):
    return render(request, "class/herb.html")

    
# 변신술
def shifter(request):
    return render(request, "class/shifter.html")

