from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from member.models import Characters
from users.models import CharInfo
from django.contrib.auth.decorators import login_required
# Create your views here.



def signup(request):
    names=[]
    all_charac = Characters.objects.values_list('charEngName', flat=True)

    for fullname in all_charac:
        names.append(fullname.split()[0].lower())
    print(names)

    if request.method == "POST":
        commucode = request.POST['commucode']
        print(request.POST['username'].lower(),commucode)
        if request.POST['password1']==request.POST['password2'] and commucode == "WT" and request.POST['username'].lower() in names:
            Newuser = User.objects.create_user(request.POST['username'], password=request.POST['password1'])            
            auth.login(request,Newuser)

            targetName = ""
            for fullname in all_charac:
                if request.POST['username'].lower() == fullname.split()[0].lower():
                    targetName = fullname

            user = request.user
            char = CharInfo(user=user,
                            char=Characters.objects.get(charEngName=targetName),
                            galeon=5,
                            classToken=0,
                            searchDone=0,)
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