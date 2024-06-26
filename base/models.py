from django.db import models
from django.contrib.auth.models import User

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