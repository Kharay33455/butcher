from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import *
import random


# Create your views here.

def base(request):
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor}
        return render(request, 'base/home.html', context)

    context ={}
    return render(request, 'base/home.html', context)

def about_us(request):
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor}
        return render(request, 'base/about-us.html', context)

    context = {}
    return render(request, 'base/about-us.html', context)

def principles(request):
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor}
        return render (request, 'base/principles.html', context)

    context ={}
    return render(request, 'base/principles.html', context)

def history(request):
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor}
        return render(request, 'base/history.html', context)

    context = {}
    return render(request, 'base/history.html', context)

def global_impact(request):
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor}
        return render(request, 'base/global-impact.html', context)

    context ={}
    return render(request, 'base/global-impact.html', context)

def business(request):
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor}
        return render(request, 'base/business.html', context)

    context ={}
    return render(request, 'base/business.html', context)


def news(request):
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor}
        return render(request, 'base/news.html', context)

    context ={}
    return render(request, 'base/news.html', context)

def kis(request):
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor}
        return render(request, 'base/kis.html', context)

    context ={}
    return render(request, 'base/kis.html', context)

def sustainability(request):
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor}
        return render(request, 'base/sustainability.html', context)

    context = {}
    return render(request,'base/sustainability.html', context)

def capitalism(request):
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor}
        return render(request, 'base/capitalism.html', context)

    context ={}
    return render(request, 'base/capitalism.html', context)

def disclaimer(request):
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor}
        return render(request, 'base/disclaimer.html', context)
    
    context = {}
    return render(request, 'base/disclaimer.html', context)

def investing(request):
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        account_types = Account_Type.objects.filter()
        

        context ={'investor':investor, 'account_types':account_types}
        return render(request, 'base/investing.html', context)
    account_types = Account_Type.objects.all()
    context = {'account_types':account_types}
    return render(request, 'base/investing.html', context)

def login_request(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            usernames = username.replace(" ","")
            password = request.POST['password1']
            passwords = password.replace(' ','')
            user = authenticate(request, username = usernames, password = passwords)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('base:investing'))
            else:
                context = {'err':'Invalid username or password'}
                return render(request, 'base/login.html', context)
        except (KeyError, Investor.DoesNotExist):
            context = {'err':'User Does Not Exist'}
            return render(request, 'base/login.html', context)
    else:

        return render(request, 'base/login.html')
def register_request(request):
    #checking if method is post
    if request.method == 'POST':
        try:
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            first_name = first_name.replace(' ','')
            last_name = last_name.replace(' ','')
            username = username.replace(' ','')
            email = email.replace(' ','')
            password1 = password1.replace(' ','')
            password2 = password2.replace(' ','')
            if password1 == password2:

                new_user = User.objects.create_user(username=username, first_name = first_name, 
                                                    last_name =last_name, password=password1, email= email)
                new_user.save()
                investor = Investor.objects.create(user = new_user, first_name = first_name,
                                                    last_name = last_name, investor_id=username)
                login(request, new_user)
                return HttpResponseRedirect(reverse('base:investing'))
            else:
                context = {'err':'Your passwords didn\'t match'}
                return render (request, 'base/register.html', context)
        except (IntegrityError):
            context = {'err': 'A user with this username already exists.'}
            return render(request, 'base/register.html', context)
    context = {}
    return render(request, 'base/register.html', context)



def logout_request(request):
    logout(request)
    return HttpResponseRedirect(reverse('base:home'))


def investments(request):
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        accounts = Account.objects.filter(investor = investor)
        total_bal =[]
        total_payout =[]
        for acc in accounts:
            if acc.is_active:
                total_bal.append(acc.balance)
                acc.roi = ((acc.account_type.return_rate +investor.referrals) * acc.level.multiplier/100) * acc.balance
                total_payout.append(acc.roi)
            else:
                acc.eroi = ((acc.account_type.return_rate +investor.referrals) * acc.level.multiplier/100) * acc.balance
        total_payout = sum(total_payout)
        total_bal = sum(total_bal)    

        
        context = {'investor':investor, 'accounts':accounts, 'total_bal': total_bal, 'total_roi': total_payout}
        return render(request, 'base/investments.html', context)
    
    else:
        return HttpResponseRedirect(reverse('base:login'))
    
def create_account(request):
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        if request.method == 'POST':
            t_id = random.randint(11111111, 99999999)
            t_id = str(t_id)
            acn = str(investor.investor_id)
            number = f'{t_id + acn}'
            acc_type = request.POST['Account_type']
            account_type = Account_Type.objects.get(name = acc_type)
            lev = request.POST['level']
            level = Level.objects.get(name = lev)
            balance = account_type.min_deposit * level.multiplier
            new_account = Account.objects.create(investor = investor, number=number,
                                                 account_type =account_type, level=level,
                                                 balance=balance)
            new_account.save()
            return HttpResponseRedirect(reverse('base:investments'))
        else:




            investor = Investor.objects.get(user = request.user)
            account_types = Account_Type.objects.all()
            levels = Level.objects.all()
            context = {'investor':investor, 'acc_types':account_types, 'levels':levels}
            return render(request, 'base/create-account.html', context)
    
    else:
        return HttpResponseRedirect(reverse('base:login'))
    

def activate(request, number):
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        acc = Account.objects.get(number = number)
        wallets = Wallet.objects.all()
        context = {'investor':investor, 'acc':acc, 'wallets':wallets}
        return render(request, 'base/activate.html', context)




    else:
        return HttpResponseRedirect(reverse('base:login'))
    

def delete(request, number):
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        acc = Account.objects.get(number = number)
        acc.delete()
        return HttpResponseRedirect(reverse('base:investments'))
    else:
        return HttpResponseRedirect(reverse('base:login'))
    

def pending(request, number):
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        acc = Account.objects.get(number = number)
        acc.is_pending = True
        acc.save()
        print(acc.is_pending)
        return HttpResponseRedirect(reverse('base:investments'))
    else:
        return HttpResponseRedirect(reverse('base:login'))
    

def profile(request):
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        accounts = Account.objects.filter(investor=investor)
        active_accounts =[]
        inactive_accounts = []
        for acc in accounts:
            if acc.is_active == True:
                active_accounts.append(acc)
            else:
                inactive_accounts.append(acc)
        active_accounts = len(active_accounts)
        inactive_accounts= len(inactive_accounts)
        context = {'investor':investor, 'aa':active_accounts, 'in':inactive_accounts}
        return render(request, 'base/profile.html', context)
    
    else:
        return HttpResponseRedirect(reverse('base:login'))