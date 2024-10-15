from django.shortcuts import render,redirect
from member.models import Characters
# Create your views here.

def member_profile(request, charID):
    char = Characters.objects.get(charID=charID)
    
    context = {
        'charID': charID,
        'char': char
    }
    
    return render(request, "profile/member_profile.html", context)

def member_main(request):
    return render(request, "profile/member_main.html")
