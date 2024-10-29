from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from member.models import Characters
from users.models import CharInfo
from django.contrib.auth.decorators import login_required
# Create your views here.


def signup(request):
    all_char_ids = Characters.objects.values_list('charID', flat=True)
    print(all_char_ids)
    if request.method == "POST":
        charcode = request.POST['charCode']
        print(charcode)
        if request.POST['password1']==request.POST['password2'] and charcode in all_char_ids:
            Newuser = User.objects.create_user(request.POST['username'], password=request.POST['password1'])            
            auth.login(request,Newuser)
            
            user = request.user
            char = CharInfo(user=user,
                            char=Characters.objects.get(charID=charcode),
                            galeon=5,
                            classToken=0,
                            searchDone=0,
                            searchCount=0,
                            classCount=0)
            char.save()
            
            return redirect('main:main_page')
    return render(request,'registration/signup.html')



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main:main_page')
        else:
            return render(request,'registration/login.html', {'error':'잘못되었습니다'})
    else:
        return render(request,'registration/login.html')