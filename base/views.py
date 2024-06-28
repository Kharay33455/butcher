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
        company_name = Company_name.objects.first()
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor, 'company_name':company_name}
        return render(request, 'base/home.html', context)

    else:
        company_name = Company_name.objects.first()
        context ={'company_name':company_name}
        return render(request, 'base/home.html', context)

def about_us(request):
    if request.user.is_authenticated:
        company_name = Company_name.objects.first()
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor, 'company_name':company_name}
        return render(request, 'base/about-us.html', context)
    else:
        company_name = Company_name.objects.first()
        context = {'company_name':company_name}
        return render(request, 'base/about-us.html', context)

def principles(request):
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        company_name = Company_name.objects.first()
        context ={'investor':investor, 'company_name':company_name}
        return render (request, 'base/principles.html', context)
    company_name = Company_name.objects.first()
    context ={'company_name':company_name}
    return render(request, 'base/principles.html', context)

def history(request):
    if request.user.is_authenticated:
        company_name = Company_name.objects.first()
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor, 'company_name':company_name}
        return render(request, 'base/history.html', context)
    company_name = Company_name.objects.first()
    context = {'company_name':company_name}
    return render(request, 'base/history.html', context)

def global_impact(request):
    company_name = Company_name.objects.first()
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor, 'company_name':company_name}
        return render(request, 'base/global-impact.html', context)

    context ={'company_name':company_name}
    return render(request, 'base/global-impact.html', context)

def business(request):
    company_name = Company_name.objects.first()
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor, 'company_name':company_name}
        return render(request, 'base/business.html', context)

    context ={ 'company_name':company_name}
    return render(request, 'base/business.html', context)


def news(request):
    company_name = Company_name.objects.first()
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor, 'company_name':company_name}
        return render(request, 'base/news.html', context)

    context ={'company_name':company_name}
    return render(request, 'base/news.html', context)

def kis(request):
    company_name = Company_name.objects.first()
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor, 'company_name':company_name}
        return render(request, 'base/kis.html', context)

    context ={ 'company_name':company_name}
    return render(request, 'base/kis.html', context)

def sustainability(request):
    company_name = Company_name.objects.first()
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor, 'company_name':company_name}
        return render(request, 'base/sustainability.html', context)

    context = { 'company_name':company_name}
    return render(request,'base/sustainability.html', context)

def capitalism(request):
    company_name = Company_name.objects.first()
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor,'company_name':company_name}
        return render(request, 'base/capitalism.html', context)

    context ={'company_name':company_name}
    return render(request, 'base/capitalism.html', context)

def disclaimer(request):
    company_name = Company_name.objects.first()
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor, 'company_name':company_name}
        return render(request, 'base/disclaimer.html', context)
    
    context = { 'company_name':company_name}
    return render(request, 'base/disclaimer.html', context)

def investing(request):
    company_name = Company_name.objects.first()
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        account_types = Account_Type.objects.filter()
        

        context ={'investor':investor, 'account_types':account_types, 'company_name':company_name}
        return render(request, 'base/investing.html', context)
    account_types = Account_Type.objects.all()
    context = {'account_types':account_types, 'company_name':company_name}
    return render(request, 'base/investing.html', context)

def login_request(request):
    company_name = Company_name.objects.first()
    if request.method == 'POST':
        try:
            if "@" in request.POST['username']:
                try:
                    possible_user = User.objects.get(email = request.POST['username'])
                    usernames = possible_user.username
                except(KeyError, User.DoesNotExist):
                    usernames = request.POST['username']
            else:

                username = request.POST['username']
                usernames = username.replace(" ","")
            password = request.POST['password1']
            passwords = password.replace(' ','')
            user = authenticate(request, username = usernames, password = passwords)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('base:investing'))
            else:
                context = {'err':'Invalid username or password', 'company_name':company_name}
                return render(request, 'base/login.html', context)
        except (KeyError, Investor.DoesNotExist):
            context = {'err':'User Does Not Exist', 'company_name':company_name}
            return render(request, 'base/login.html', context)
    else:

        return render(request, 'base/login.html')
def register_request(request):
    company_name = Company_name.objects.first()
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
                context = {'err':'Your passwords didn\'t match', 'company_name':company_name}
                return render (request, 'base/register.html', context)
        except (IntegrityError):
            context = {'err': 'A user with this username already exists.', 'company_name':company_name}
            return render(request, 'base/register.html', context)
    context = {'company_name':company_name}
    return render(request, 'base/register.html', context)



def logout_request(request):
    company_name = Company_name.objects.first()
    logout(request)
    return HttpResponseRedirect(reverse('base:home'))


def investments(request):
    company_name = Company_name.objects.first()
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

        
        context = {'investor':investor, 'accounts':accounts, 'total_bal': total_bal, 'total_roi': total_payout, 'company_name':company_name}
        return render(request, 'base/investments.html', context)
    
    else:
        return HttpResponseRedirect(reverse('base:login'))
    
def create_account(request):
    company_name = Company_name.objects.first()
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        if request.method == 'POST':
            t_id = random.randint(1111111111111111, 9999999999999999)
            t_id = str(t_id)
            number = f'{t_id}'
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
            context = {'investor':investor, 'acc_types':account_types, 'levels':levels, 'company_name':company_name}
            return render(request, 'base/create-account.html', context)
    
    else:
        return HttpResponseRedirect(reverse('base:login'))
    

def activate(request, number):
    company_name = Company_name.objects.first()
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        acc = Account.objects.get(number = number, investor=investor)
        wallets = Wallet.objects.all()
        context = {'investor':investor, 'acc':acc, 'wallets':wallets, 'company_name':company_name}
        return render(request, 'base/activate.html', context)




    else:
        return HttpResponseRedirect(reverse('base:login'))
    

def delete(request, number):
    company_name = Company_name.objects.first()
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        acc = Account.objects.get(number = number)
        acc.delete()
        return HttpResponseRedirect(reverse('base:investments'))
    else:
        return HttpResponseRedirect(reverse('base:login'))
    

def pending(request, number):
    company_name = Company_name.objects.first()
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
    company_name = Company_name.objects.first()
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
        context = {'investor':investor, 'aa':active_accounts, 'in':inactive_accounts, 'company_name':company_name}
        return render(request, 'base/profile.html', context)
    
    else:
        return HttpResponseRedirect(reverse('base:login'))
    

def letter(request):
    if request.user.is_authenticated:
        company_name = Company_name.objects.first()
        investor = Investor.objects.get(user = request.user)
        context ={'investor':investor, 'company_name':company_name}
        return render(request, 'base/letter.html', context)

    else:
        company_name = Company_name.objects.first()
        context ={'company_name':company_name}
        return render(request, 'base/letter.html', context)
    
"""support"""
def support(request):
    company_name = Company_name.objects.first()
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        tickets = Ticket.objects.filter(investor = investor)
        context = {'investor':investor, 'company_name':company_name,'tickets':tickets}
        return render(request, 'base/support.html', context)
    else:
        return HttpResponseRedirect(reverse('base:login'))
    

"""Ticket"""

def ticket(request, number):
    company_name = Company_name.objects.first()
    if request.user.is_authenticated:
        investor = Investor.objects.get(user = request.user)
        ticket = Ticket.objects.get(ticket_id = number, investor= investor)
        if request.method == 'POST':
            if request.FILES:
                image = request.FILES['image']
                body = request.POST['body']
                new_message = Message.objects.create(ticket = ticket, body=body, image=image)


                return HttpResponseRedirect(reverse('base:ticket', args=[number]))
            else:
                if request.POST['body'].strip()=="":
                    return HttpResponseRedirect(reverse('base:ticket', args=[number]))
                else:

                    body = request.POST['body']
                    new_message = Message.objects.create(ticket = ticket, body=body)
                
                    return HttpResponseRedirect(reverse('base:ticket', args=[number]))
                
        
        else:
            ticket.is_read = True
            investor.has_new_message = False
            ticket.save()
            investor.save()
            messages = Message.objects.filter(ticket = ticket).order_by('time_sent')

            context = {'investor':investor, 'company_name':company_name, 'ticket':ticket, 'messages':messages}
            return render(request, 'base/ticket.html', context)
    else:
        return HttpResponseRedirect(reverse('base:login'))    
    
def new_issue(request):
    
    if request.user.is_authenticated:
        request.method =='POST'
        investor = Investor.objects.get(user = request.user)
        ticket_id = random.randint(111111111111111111,9999999999999999999)
        subject = request.POST['subject']
        support = Support.objects.order_by('?').first()
        new_ticket = Ticket.objects.create(ticket_id = ticket_id, subject=subject, investor=investor, support = support, is_read = True)
        body = request.POST['body']
        new_message = Message.objects.create(ticket = new_ticket, body=body)
        reply_message = Message.objects.create(ticket=new_ticket, body ='We will reply you shortly. Note; This message is auto-generated.', from_support = True)
        return HttpResponseRedirect(reverse('base:ticket', args= [ticket_id]))        
    else:
        return HttpResponseRedirect(reverse('base:login'))
