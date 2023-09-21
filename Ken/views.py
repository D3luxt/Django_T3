from django.shortcuts import render
from django.http.response import responses
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.shortcuts import *
from .forms import *
from django.db import models
from advice.models import *
from advice.models import productitem
from django.db.models import Sum
import sweetify

# Create your views here.
def main(request):
    return render(request, 'register.html')

def index(request):
    return render(request, 'index.html')

def source(request):
    return render(request, 'source.html')

def objective(request):
    return render(request, 'objective.html')

#def allproduct(request,pro_id):
    #return render(request, 'allproduct.html',context={'pro_id':pro_id})

@login_required
def dashboard(request):
    form = User.objects.get(id=request.user.id)
    try:
        exform = usernotebook.objects.get(accountlink=form.id)
        return render(request, 'dashboard.html', {'exform': exform, 'form': form})
    except:
        pass
    return render(request, 'dashboard.html',{'form': form})

@login_required
def productupdate(request, pro_id):
    if not request.user.is_superuser:
        return HttpResponse(status=403)
    else:
        product = productitem.objects.get(pro_id=pro_id)
        if request.method == 'POST':
            form = ProAddAdmin(request.POST,request.FILES,instance=product)
            if form.is_valid():
                print('save complete')
                form.save()
                return HttpResponseRedirect(reverse('productshow'))
        else:
            form = ProAddAdmin(instance=product)
        context = {'form': form, }
        return render(request, 'productupdate.html', context)

@login_required
def productdelete(request, pro_id):
    if not request.user.is_superuser:
        return HttpResponse(status=403)
    else:
            product = productitem.objects.get(pro_id=pro_id)
            product.delete()
            return HttpResponseRedirect(reverse('productshow'))


@login_required
def profile(request):
    if request.POST:
        form = UserDetail(request.POST,instance=request.user)
        is_new_profile = False
        try:
            ex_form = UserDetailExtended(request.POST,request.FILES,instance=request.user.usernotebook)
        except:
            ex_form = UserDetailExtended(request.POST,request.FILES)
            is_new_profile = True
        if form.is_valid() and ex_form.is_valid():
            form.save()
            if is_new_profile:
                profile = ex_form.save(commit=False)
                profile.accountlink = request.user
                profile.save()
            else:
                ex_form.save()
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = UserDetail()
        ex_form = UserDetailExtended()
    context = {'form':form,'ex_form':ex_form}
    return render(request,'profile.html',context)

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('dashboard'))
    else:
        if request.method=='POST':
            form = UserCre(request.POST)
            if form.is_valid():
                print(form)
                user = form.save()
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            form = UserCre()
        context = {'form':form,}
        return render(request,'register.html',context)

@login_required
def productconfig(request):
    if request.method == 'POST':
        if request.user.is_superuser:
            form = ProAddAdmin(request.POST,request.FILES)
            if form.is_valid():
                print(form)
                proadder = form.save(commit=False)
                proadder.id_link = request.user
                proadder.save()
                return HttpResponseRedirect(reverse('productshow'))
        else:
            form = ProAdd(request.POST, request.FILES)
            if form.is_valid():
                print(form)
                proadder = form.save(commit=False)
                proadder.id_link = request.user
                proadder.save()
                return HttpResponseRedirect(reverse('productshow'))
    else:
        form = ProAddAdmin()
    context = {'form': form, }
    return render(request, 'productconfig.html', context)


def productshow(request):
    my_data = productitem.objects.all()  # for all the records
    context = {
        'my_data': my_data,
    }
    return render(request, 'productshow.html', context)

@login_required
def showUser(request,id):
    if not request.user.is_superuser:
        return HttpResponse(status=403)
    else:
        user_id = User.objects.get(id=id)
        user_extend = usernotebook.objects.get(accountlink = id)
        return render(request, 'showUser.html',{'user_extend':user_extend,'user_id':user_id})

def showProduct(request,id):
    pro_id = productitem.objects.get(pro_id=id)
    return render(request, 'showProduct.html',{'pro_id':pro_id,})

@login_required
def showOrder(request,id):
    if not request.user.is_superuser:
        return HttpResponse(status=403)
    else:
        or_id = ordernotebook.objects.get(or_id=id)
        return render(request, 'showOrder.html',{'or_id':or_id,})

@login_required
def ordershow(request):
    if not request.user.is_superuser:
        return HttpResponse(status=403)
    else:
        my_data = ordernotebook.objects.all()  # for all the records
        context = {
            'my_data': my_data,
        }
        return render(request, 'ordershow.html', context)

def orderApproved(request, or_id,pro_id_id):
    if not request.user.is_superuser:
        return HttpResponse(status=403)
    else:
        pro_status = productitem.objects.get(pro_id=pro_id_id)
        order_status = ordernotebook.objects.get(or_id=or_id)
        pro_status.amount = 'sold'
        order_status.status = 'approved'
        pro_status.save()
        order_status.save()
        return HttpResponseRedirect(reverse('ordershow'))

def orderApproved(request, or_id,pro_id_id):
    if not request.user.is_superuser:
        return HttpResponse(status=403)
    else:
        pro_status = productitem.objects.get(pro_id=pro_id_id)
        order_status = ordernotebook.objects.get(or_id=or_id)
        pro_status.amount = 'sold'
        order_status.status = 'approved'
        pro_status.save()
        order_status.save()
        return HttpResponseRedirect(reverse('ordershow'))

def orderApproved(request, or_id,pro_id_id):
    if not request.user.is_superuser:
        return HttpResponse(status=403)
    else:
        pro_status = productitem.objects.get(pro_id=pro_id_id)
        order_status = ordernotebook.objects.get(or_id=or_id)
        pro_status.amount = 'sold'
        order_status.status = 'approved'
        pro_status.save()
        order_status.save()
        return HttpResponseRedirect(reverse('ordershow'))


def orderRejected(request, or_id):
    if not request.user.is_superuser:
        return HttpResponse(status=403)
    else:
        order_status = ordernotebook.objects.get(or_id=or_id)
        order_status.status = 'rejected'
        order_status.save()
        return HttpResponseRedirect(reverse('ordershow'))


def productRejected(request, pro_id):
    if not request.user.is_superuser:
        return HttpResponse(status=403)
    else:
        order_status = productitem.objects.get(pro_id=pro_id)
        order_status.approvedstatus = 'rejected'
        order_status.save()
        return HttpResponseRedirect(reverse('productshow'))


def productApproved(request, pro_id):
    if not request.user.is_superuser:
        return HttpResponse(status=403)
    else:
        pro_status = productitem.objects.get(pro_id=pro_id)
        pro_status.approvedstatus = 'approved'
        pro_status.save()
        return HttpResponseRedirect(reverse('productshow'))


@login_required
def productBuy(request,pro_id):
    pro_id = productitem.objects.get(pro_id=pro_id)

    #price = productitem.objects.get(price=price)

    if request.method == 'POST':
            form = OrderAdd(request.POST, request.FILES)
            if form.is_valid():
                print(form)
                proadder = form.save(commit=False)
                proadder.u_id = request.user
                proadder.pro_id = pro_id

                #proadder.or_sale = price

                proadder.save()
                return HttpResponseRedirect(reverse('probuyhistory'))
    else:
        form = OrderAdd()
    context = {'form': form,'pro_id':pro_id, }
    return render(request, 'productBuy.html', context)

@login_required
def paymentAdd(request):

    if request.method == 'POST':
        if request.user.is_superuser:
            form = paymentMethodForm(request.POST)
            if form.is_valid():
                print(form)
                form.save()
                return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse(status=403)
    else:
        form = paymentMethodForm()
    showpay = paymentMethod.objects.all()
    context = {'form': form,'showpay':showpay }


    return render(request, 'payment_add.html', context)

@login_required
def proaddhistory(request):
    my_data = productitem.objects.filter(id_link=request.user)  # for all the records
    context = {
        'my_data': my_data,
    }
    return render(request, 'proaddhistory.html', context)

@login_required
def totalsalesaveweb(request):
    if not request.user.is_superuser:
        return HttpResponse(status=403)
    else:
        enter_form = sumsalevalue(request.POST)
        form = ordernotebook.objects.filter(saveyet='notyet',status='approved').aggregate(total=Sum('or_sale'))
        formcount = ordernotebook.objects.filter(saveyet='notyet',status='approved').count()
        if request.method == 'POST':
            if request.user.is_superuser:
                form = sumsalevalue(request.POST)
                if form.is_valid():
                    print(form)
                    form.save()
                    ordernotebook.objects.all().update(saveyet='saved')
                    return HttpResponseRedirect(reverse('totalsalesaveweb'))
        showtransaction = totaltransaction.objects.all()
        context = {
            'form':form,
            'formcount':formcount,
            'enter_form':enter_form,
            'showtransaction':showtransaction,
        }
    return render(request, 'totalsalesaveweb.html',context)

@login_required
def totalsaveED(request,save):
    if not request.user.is_superuser:
        return HttpResponse(status=403)
    else:
        save_status = ordernotebook.objects.get(saveyet=save)
        save_status.saveyet = 'saved'

        return HttpResponseRedirect(reverse('totalsalesaveweb'))

@login_required
def probuyhistory(request):
    my_data = ordernotebook.objects.filter(u_id=request.user)  # for all the records
    context = {
        'my_data': my_data,
    }
    return render(request, 'probuyhistory.html', context)

####
def about(request):
    return render(request, 'about.html')

def p01(request):
    sweetify.success(request, 'You did it', text='Good job! You successfully showed a SweetAlert message', persistent='Hell yeah')
    return render(request, 'p01.html')

