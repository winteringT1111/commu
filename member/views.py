from django.shortcuts import render,redirect
from member.models import Characters, Inventory
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/')
def member_profile(request, charID):
    char = Characters.objects.get(charID=charID)
    inven = Inventory.objects.filter(user_id=request.user)
    
    context = {
        'charID': charID,
        'char': char,
        'inven':inven
    }
    
    return render(request, "profile/member_profile.html", context)

def member_main(request):
    return render(request, "profile/member_main.html")
