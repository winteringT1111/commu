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
    gift_list = Gift.objects.filter(receiver_user=request.user).order_by('orderDate')
    
    context = {
        'gifts':gift_list
    }
    
    return render(request, "gift/giftbox.html",context)
