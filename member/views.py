from django.shortcuts import render,redirect
from member.models import Characters, Inventory, Gift,Inventory_magic
from users.models import CharInfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator


@login_required(login_url='/')
def member_profile(request, charName):

    char = Characters.objects.get(charFirstName=charName.capitalize())
    characinfo = CharInfo.objects.get(char=char)
    inven = Inventory.objects.filter(user_id=characinfo.user)    
    inven2 = Inventory_magic.objects.filter(user_id=characinfo.user)
    combined = list(inven) + list(inven2)
    
    paginator = Paginator(combined, 25) 
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    pages_items = [paginator.page(i).object_list for i in paginator.page_range]
    print("--------------",pages_items)
    
    context = {
        'charname': charName,
        'char': char,
        'inven':combined,
        "page_obj": page_obj, 
        "pages_items": pages_items
    }
    
    return render(request, "profile/member_profile.html", context)

@login_required(login_url='/')
def member_main(request):
    chars = Characters.objects.all().order_by('charFirstName')
    
    context = {
        'chars': chars
    }
    
    return render(request, "profile/member_main.html",context)


@login_required(login_url='/')
def giftbox(request):
    getUser = request.user
    gift_list = Gift.objects.filter(receiver_user=request.user).order_by('orderDate')
    
    if request.method == "POST":
        gift_id = request.POST['giftidnum']
        target = Gift.objects.get(giftID=gift_id)

        all_items = Inventory.objects.filter(user_id=getUser).values_list('itemInfo', flat=True)
        item = target.itemInfo
            
        if item.itemID in all_items:
            update_item = Inventory.objects.get(itemInfo=item, user=getUser)
            update_item.itemCount += target.itemCount
            update_item.save()
        else:
            inven = Inventory(itemCount=target.itemCount,
                            itemInfo=item,
                            user=getUser)
            inven.save()

        target.accepted = True
        target.save()


    context = {
        'gifts':gift_list
    }
    
    return render(request, "gift/giftbox.html",context)
