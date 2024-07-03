from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Account_Type(models.Model):
    name = models.CharField(max_length=80)
    min_deposit = models.IntegerField()
    min_holding_term = models.IntegerField()
    return_rate = models.IntegerField()
    about = models.TextField(max_length=1500)
    link = models.SlugField(max_length=80)
    is_alternate = models.BooleanField()

    def __str__(self):
        return f'{self.name} Account'
    
class Level(models.Model):
    name = models.CharField(max_length=20)
    multiplier = models.DecimalField(default=1.0, decimal_places=2, max_digits=5)

    def __str__(self):
        return f'{self.name} Class'

class Investor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    investor_id = models.CharField(max_length=10)
    referrals = models.IntegerField(default=0)
    holdings = models.IntegerField(default=0)
    earnings = models.IntegerField(default=0)
    level = models.CharField(default='Silver', max_length=10)
    has_new_message = models.BooleanField(default=False)
    withdrawal_pin = models.CharField(blank=True, null=True, max_length=6)
    def __str__(self):
        return f'{self.first_name} {self.last_name}, user {self.investor_id}'

class Account(models.Model):
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    number = models.CharField(max_length=20)
    account_type = models.ForeignKey(Account_Type, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    roi = models.IntegerField(null=True, blank=True)
    eroi = models.IntegerField(null = True, blank=True)
    is_active = models.BooleanField(default=False)
    activation_date = models.DateField(null=True, blank=True)
    is_pending = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.investor.investor_id} {self.account_type.name} {self.level.name} Account'
    

class Wallet(models.Model):
    currency = models.CharField(max_length=10)
    network = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.currency} {self.network} wallet'

class Company_name(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f'Current company name is {self.name}'
    
"""Implementing the support function"""
class Support(models.Model):
    name = models.CharField(max_length=10)
    location = models.CharField(max_length=20)
    pfp = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.name}'
    
class Ticket(models.Model):
    ticket_id = models.CharField(max_length=20)
    subject = models.CharField(max_length=30)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    support = models.ForeignKey(Support, on_delete=models.CASCADE)
    is_read= models.BooleanField(default=False)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.subject} ticket by {self.investor.user.username} on {self.date_of_creation}//Is read? {self.is_read}'
    

class Message(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete = models.CASCADE)
    body = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    from_support = models.BooleanField(default=False)
    time_sent = models.DateTimeField(auto_now_add=True)
    is_replied = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        if self.from_support == True:
            self.ticket.is_read = False
            self.ticket.save()
            self.ticket.investor.has_new_message = True
            self.ticket.investor.save()
        super(Message, self).save(*args, **kwargs)

    def __str__(self):
        if self.from_support == True:
            return f'Reply to {self.ticket.investor.first_name} {self.ticket.investor.last_name} / is_replied? {self.is_replied}'
        else:
            return f'Message from {self.ticket.investor.first_name} {self.ticket.investor.last_name} / is_replied? {self.is_replied}'


class Withdrawal_request(models.Model):
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    withdrawal_id = models.CharField(max_length=20)
    amount = models.IntegerField()
    wallet_type = models.CharField(max_length=10)
    wallet_address = models.CharField(max_length=40)
    date_placed = models.DateTimeField(auto_now_add=True)
    is_pending = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.withdrawal_id}'