from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth import logout
from .models import Poll
from  django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
# Create your views here.
def home(request):
    polls = Poll.objects.all().order_by("-pk")
    return render(request, 'Pollsapp/base.html', {'polls':polls})

def log_out(request):
    logout(request)
    return redirect('Home')
@login_required(login_url='https://accounts.google.com/o/oauth2/auth/oauthchooseaccount?client_id=6147124210-1tioi8jg0vm4s5qsl39piksl8k5fvsbr.apps.googleusercontent.com&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Faccounts%2Fgoogle%2Flogin%2Fcallback%2F&scope=email%20profile&response_type=code&state=j188cVFQFUh7&access_type=online&flowName=GeneralOAuthFlow')
def create_poll(request):
    if request.method=='POST':
        poll = Poll(poll=request.POST["question"], op1=request.POST["op1"], op2=request.POST["op2"], op3=request.POST["op3"], user = request.user)
        poll.save()
        messages.success(request, 'Poll created ! ')
    return redirect('Home')
@login_required(login_url='https://accounts.google.com/o/oauth2/auth/oauthchooseaccount?client_id=6147124210-1tioi8jg0vm4s5qsl39piksl8k5fvsbr.apps.googleusercontent.com&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Faccounts%2Fgoogle%2Flogin%2Fcallback%2F&scope=email%20profile&response_type=code&state=j188cVFQFUh7&access_type=online&flowName=GeneralOAuthFlow')
def vote(request, id):
    poll = Poll.objects.get(pk=id)
    if request.method=='POST':
        if request.POST["optradio"]=='op1':
            poll.op1_cnt+=1
        elif request.POST["optradio"]=='op2':
            poll.op2_cnt+=1
        elif request.POST["optradio"]=='op3':
            poll.op3_cnt+=1
        poll.save()
        return redirect('result', id=id)
@login_required(login_url='https://accounts.google.com/o/oauth2/auth/oauthchooseaccount?client_id=6147124210-1tioi8jg0vm4s5qsl39piksl8k5fvsbr.apps.googleusercontent.com&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Faccounts%2Fgoogle%2Flogin%2Fcallback%2F&scope=email%20profile&response_type=code&state=j188cVFQFUh7&access_type=online&flowName=GeneralOAuthFlow')
def result(request, id):
    poll = Poll.objects.get(pk=id)
    return render(request, "Pollsapp/result.html", {'poll':poll})