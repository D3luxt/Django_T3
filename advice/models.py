from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.utils.timezone import now
from django import forms

from django.db.models import Sum

# Create your models here.

class usernotebook(models.Model):
    user_id = models.BigAutoField(primary_key=True,auto_created=True,serialize=False)
    gender = models.CharField(max_length=15)
    phone = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to='images/',blank=True)
    accountlink = models.OneToOneField(User,on_delete=models.CASCADE)

class productitem(models.Model):
    pro_id = models.BigAutoField(primary_key=True,auto_created=True,serialize=False)
    pro_name = models.CharField(max_length=45)
    brand = models.CharField(max_length=45)
    pro_desc = models.CharField(max_length=255,blank=True,)
    price = models.IntegerField(default=0)
    amount = models.CharField(max_length=15,default='instock',blank=True)
    approvedstatus = models.CharField(max_length=15,default='waiting',blank=True)
    date_add = models.DateField(default=now, editable=False)
    pro_pic = models.ImageField(upload_to='images/',blank=True)
    id_link = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pro_id)


class paymentMethod(models.Model):
    bank_account_number = models.CharField(max_length=45,primary_key=True)
    bank_account = models.CharField(max_length=45)

    def __str__(self):
        return self.bank_account_number

class ordernotebook(models.Model):
    or_id = models.BigAutoField(primary_key=True,auto_created=True,serialize=False)
    date_buy = models.DateField(default=now, editable=False)
    or_sale = models.FloatField(default=0.0)
    u_id = models.ForeignKey(User, on_delete=models.CASCADE,editable=False,default='')
    pro_id = models.ForeignKey(productitem,on_delete=models.CASCADE)
    deli_address = models.CharField(max_length=45,blank=False)
    bank_select = models.ForeignKey(paymentMethod,on_delete=models.CASCADE)
    payslip_pic = models.ImageField(upload_to='payslip/', blank=True)
    status = models.CharField(max_length=45, default='waiting')
    saveyet = models.CharField(max_length=45,default='notyet')

class totaltransaction(models.Model):
    trans_id = models.BigAutoField(primary_key=True,auto_created=True,serialize=False)
    totalsale = models.CharField(max_length=45)
    totalorder = models.CharField(max_length=45)
    date_save = models.DateField(default=now, editable=False)