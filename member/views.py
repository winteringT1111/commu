from django.shortcuts import render,redirect
from member.models import Characters, Inventory, Gift
from users.models import CharInfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='/')
def member_profile(request, username):
    user = User.objects.get(username=username)
    charac = CharInfo.objects.get(user=user)
    inven = Inventory.objects.filter(user_id=user)
    
    context = {
        'username': username,
        'char': charac.char,
        'inven':inven
    }
    
    return render(request, "profile/member_profile.html", context)

def member_main(request):
    return render(request, "profile/member_main.html")


def giftbox(request):
    getUser = request.user
    gift_list = Gift.objects.filter(receiver_user=request.user).order_by('orderDate')
    
    if request.method == "POST":
        gift_id = request.POST['giftidnum']
        target = Gift.objects.get(giftID=gift_id)

        print(gift_id,target)

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
