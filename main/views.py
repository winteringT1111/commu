from django.shortcuts import render,redirect
from member.models import Characters,Inventory_magic,Attendance,Inventory,Inventory_potion
from users.models import CharInfo
from store.models import Item_magic,Potion,Item,PotionStatus
from django.utils import timezone
from datetime import datetime
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import random
import ast
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
# Create your views here.


@login_required(login_url='/login')
def main_page(request):
    return render(request, "main.html")

@login_required(login_url='/login')
def notice(request):
    return render(request, "notice/notice.html")

@login_required(login_url='/login')
def world(request):
    return render(request, "notice/world.html")

@login_required(login_url='/login')
def system(request):
    return render(request, "notice/system.html")

@login_required(login_url='/login')
def totalsystem(request):
    return render(request, "notice/total_system.html")


@login_required(login_url='/login')
def attendance(request):
    getUser = request.user
    char = CharInfo.objects.get(user=getUser)
    userinfo = Characters.objects.get(charID=char.char_id)
    
    # 현재 시간 확인
    current_time = timezone.localtime(timezone.now())
    current_hour = current_time.hour
    today_date = current_time.date()
    
    if request.method == "POST":
        # 출석 가능한 시간 7시 ~ 17시
        if 7 <= current_hour < 17:
            # 오늘 이미 출석한 기록이 있으면 출석 불가
            if char.attendance_date == today_date:
                show_modal = "modal2"
                modal_message = "오늘은 이미 출석을 했습니다."
            else:
                # 출석이 가능하면 출석 처리
                char.galeon += 1  # 갈레온 추가
                char.classToken += 3 # 수업토큰
                char.attendance_date = today_date  # 출석일 업데이트
                char.today_attended = True  # 금일 출석 여부 업데이트
                
                # 누적 출석 일 수 업데이트
                char.attendance_count += 1
                char.save()
                
                show_modal = "modal1"
                modal_message = "출석이 완료되었습니다."
        else:
            # 출석 시간이 아닌 경우
            show_modal = "modal2"
            modal_message = "출석 가능한 시간이 아닙니다."
        
        return JsonResponse({
            'show_modal': show_modal, 
            'modal_message': modal_message,
            'attendance_count': char.attendance_count,  # 누적 출석 일 수
            'today_attended': char.today_attended  # 금일 출석 현황
        })
    
    context = {
        'character': userinfo,
        'attendance_count': char.attendance_count,  # 템플릿에 누적 출석 일 수 전달
        'today_attended': char.today_attended  # 템플릿에 금일 출석 여부 전달
    }
    
    return render(request, "class/attendance.html", context)



    
# 수업 페이지
@login_required(login_url='/login')
def class_main(request):
    return render(request, "class/class_main.html")



# 마법의 약
@login_required(login_url='/login')
def potion(request):
    inven = Inventory_magic.objects.filter(user_id=request.user)
    paginator = Paginator(inven, 16)  # 한 페이지에 3개의 아이템

    # 페이지 번호를 가져오기
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    # 각 페이지의 아이템 목록을 생성
    pages_items = [paginator.page(i).object_list for i in paginator.page_range]
    token = CharInfo.objects.get(user=request.user).classToken
    
    try:
        status = PotionStatus.objects.get(user=request.user)
    except PotionStatus.DoesNotExist:
        status = PotionStatus(user=request.user, xp=0, degree=3)
        status.save()
        
    return render(request, "class/potion.html", {"page_obj": page_obj, "pages_items": pages_items, "token":token, "status":status})


@require_POST
def check_combination(request):
    
    char = CharInfo.objects.get(user=request.user)  # Get character data
    status = PotionStatus.objects.get(user=request.user)
    getUser = request.user
    
    try:
        # Parse the selected items from the request body
        data = json.loads(request.body)
        selected_items = data.get('selected_items', [])

        # Sort selected items to ensure order doesn't affect comparison
        selected_items_set = set(selected_items)

        # Initialize response variables
        result = "failure"
        image = "img/store/빈 물약.png"
        message = "" 

        potions = Potion.objects.all()

        for potion in potions:
            potion_recipe = set(ast.literal_eval(potion.potionRecipe))
            if selected_items_set == potion_recipe:
                # 등급 조정
                if status.degree > potion.degree:
                    break
                
                result = "success"
                image = f"img/store/{potion.itemName}.png" 
                if potion.discovered:
                    message = f"{potion.itemName} 조합에 성공했습니다!"
                    status.xp +=15
                    status.save()
                else:
                    message = f"{potion.itemName} 조합에 최초 성공했습니다!"
                    potion.discovered = True
                    potion.discoverer = request.user.username
                    status.xp +=30
                    status.save()
                
                # 인벤토리에 넣어주기
                target = potion
                all_items = Inventory_potion.objects.filter(user_id=getUser).values_list('itemInfo', flat=True)
                
                if target.itemID in all_items:
                    update_item = Inventory_potion.objects.get(itemInfo=target, user=getUser)
                    update_item.itemCount += 1
                    update_item.save()
                else:
                    inven = Inventory_potion(itemCount=1,
                                    itemInfo=target,
                                    user=getUser)
                    inven.save()    
                break 

        if result == 'failure':
            try:
                inven = Inventory.objects.get(user=request.user, itemInfo__itemName="빈 물약")
                inven.itemCount += 1
                inven.save()
            except:
                item_info = Item.objects.get(itemName="빈 물약")
                Inventory.objects.create(
                    user=request.user,
                    itemInfo=item_info,
                    itemCount=1
                )
            status.xp +=10
            status.save()
            
        # 토큰 차감
        char.classToken -= 1
        char.save()
        
        # 선택한 아이템 차감
        for item in selected_items_set:
            inven = Inventory_magic.objects.get(user=request.user, itemInfo__itemName=item)
            if int(inven.itemCount) == 1:
                inven.delete()
            else:
                inven.itemCount -= 1
                inven.save()
                
        if status.xp >= 170:
            status.degree = 2
            status.save()

        # Return the result as a JSON response
        return JsonResponse({'result': result, 'image': image, 'message':message})

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)


# 약초학
@login_required(login_url='/login')
def herb(request):
    random_herb_item = Item_magic.objects.filter(itemCategory2='약초학').order_by('?').first()
    random_number = random.randint(1, 3)
    getUser = request.user
    user = CharInfo.objects.get(user=getUser)
    
    if request.method == "POST":
        itemname = request.POST['herbname']
        count = int(request.POST['count'])
        print(itemname,count)
        
        target = Item_magic.objects.get(itemName=itemname)

        all_items = Inventory_magic.objects.filter(user_id=getUser).values_list('itemInfo', flat=True)
        
        if target.itemID in all_items:
            update_item = Inventory_magic.objects.get(itemInfo=target, user=getUser)
            update_item.itemCount += count
            update_item.save()
        else:
            inven = Inventory_magic(itemCount=count,
                            itemInfo=target,
                            user=getUser)
            inven.save()
            
        user.classToken -= 1
        user.save()
    
    
    context = {'herb': random_herb_item,
               'count': random_number,
               'token':user.classToken}
    
    return render(request, "class/herbology.html", context)

    
# 비행
@login_required(login_url='/login')
def shifter(request):
    user = CharInfo.objects.get(user=request.user)
    
    try:
        attendance = Attendance.objects.get(user=request.user)
    except Attendance.DoesNotExist:
        attendance = Attendance(user=request.user, attendance_date=None, total_attendance=0, broom_item_received=False)
        attendance.save()
        
    # 현재 시간 확인
    current_time = timezone.localtime(timezone.now())
    today_date = current_time.date()
        
    if request.method == "POST":
        if attendance.attendance_date == today_date:
            show_modal = "modal2"
            modal_message = "오늘은 이미 수업을 이수했습니다."
        else:
            attendance.attendance_date = today_date  # 출석일 업데이트
            attendance.total_attendance += 1
            attendance.save()
                
            show_modal = "modal1"
            modal_message = "비행 수업이 완료되었습니다."
            user.classToken -= 1
            user.save()
            
            if attendance.total_attendance == 7 and not attendance.broom_item_received:
                broom = Item.objects.get(itemName="빗자루")
                inven = Inventory(itemCount=1,
                            itemInfo=broom,
                            user=request.user)
                inven.save()
                attendance.broom_item_received = True
                attendance.save()
                show_modal = "modal1"
                modal_message = "빗자루 아이템이 인벤토리에 수령되었습니다."
            
        return JsonResponse({
        'show_modal': show_modal, 
        'modal_message': modal_message,
        'attendance_count': attendance.total_attendance,  # 누적 출석 일 수
        'got_broom': attendance.broom_item_received,
        'token':user.classToken
        })
    
    context = {
        'attendance_count': attendance.total_attendance,  # 템플릿에 누적 출석 일 수 전달
        'got_broom': attendance.broom_item_received,  # 템플릿에 금일 출석 여부 전달
        'token':user.classToken,
        'got_broom': attendance.broom_item_received,
    }
    
    return render(request, "class/flying.html", context)
    
    