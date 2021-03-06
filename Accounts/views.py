#coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import MyUser as User
def index(request):
	pass
def register(request):
    if request.method == 'POST':
	form = RegisterForm(request.POST)
	if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
	    sex = form.cleaned_data['sex']
	    nick_name = form.cleaned_data['nick_name']
	    real_name = form.cleaned_data['real_name']
            #由于自定义过管理器，所以不能再用父类的
            #create方法，否则将无法认证！原因是父类中的唯一身份标志是username，在这里是email!
	    User.objects.create_user(
                    email = username,
		    password = password,
		    nick_name = nick_name,
		    real_name = real_name,
                    )
	    return HttpResponse('ok')
    else:
        form = RegisterForm()
        return render(request,'accounts/register.html',{'form':form})

def log_in(request):
    if request.method == 'POST':
        email = request.POST['email']
	password = request.POST['password']
	user = authenticate(
	username = email,
	password = password,
        )
	if user is not None:
            if user.is_active:
		login(request,user)
                request.user.set_online()
                request.user.save()
	        return HttpResponse('ok')
	    else:
		pass
	else:
	        return HttpResponse(password)
    else:
        return render(request,'accounts/login.html')

@login_required
def user_info(request):
    user = request.user
    context = {
            'sex':user.get_sex(),
            'real_name':user.get_real_name(),
            'nick_name':user.get_nick_name(),
            'email':user.get_email(),
            'work':user.get_work(),
            'phone_num':user.get_phone_num(),
            'weight':user.get_weight(),
            'height':user.get_height(),
            'age':user.get_age(),
            }
    return render(request,'accounts/user_info.html',context)

@login_required
def info_edit(request):
    user = request.user
    if request.method == 'POST':
        post=request.POST
        nn=post['nick_name']
        em=post['email']
        wk=post['work']
        pn=post['phone_num']
        user.set_nick_name(nn)
        user.set_email(em)
        user.set_work(wk)
        user.set_phone_num(pn)
        user.save()
        return HttpResponse('ok')
    else:
        context = {
                'sex':user.get_sex(),
                'real_name':user.get_real_name(),
                'nick_name':user.get_nick_name(),
                'email':user.get_email(),
                'work':user.get_work(),
                'phone_num':user.get_phone_num(),
                'weight':user.get_weight(),
                'height':user.get_height(),
                'age':user.get_age(),
                }
        return render(request,'accounts/info_edit.html',context)
def log_out(request):
    request.user.set_offline()
    request.user.save()
    logout(request)
    return HttpResponse('')
    #return render(request,'accounts/logout.html')
