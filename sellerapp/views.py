from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from petsapp.models import catedb
from sellerapp.models import sellpetdb, sellersigndb


# Create your views here.
def seller_home(request):
    return render(request,"sellerhome.html")
def seller_pets(request):
    cat=catedb.objects.all()
    return render(request,"sellerpets.html",{'cat':cat})
def savesell(request):
    if request.method == "POST":
        na = request.POST.get('pname')
        brd = request.POST.get('breed')
        ag = request.POST.get('age')
        clr = request.POST.get('color')
        gen = request.POST.get('gender')
        pri = request.POST.get('price')
        adrs = request.POST.get('address')
        nm = request.POST.get('name')
        phn = request.POST.get('phone')
        ptimg = request.FILES['petimg']
        obj = sellpetdb(pname=na, breed=brd, age=ag, color=clr, gender=gen, price=pri, address=adrs,name=nm, phone=phn, petimg=ptimg)
        obj.save()
        return redirect(seller_pets)

def display_sell(request):
    data=sellpetdb.objects.filter(name=request.session['sname'])
    return render(request,"displaysell.html",{'data':data})
def edit_sale(request,dataid):
    data=sellpetdb.objects.get(id=dataid)
    return render(request,"editsale.html",{'data':data})
def update_sale(request,dataid):
    if request.method=="POST":
        na = request.POST.get('pname')
        brd = request.POST.get('breed')
        ag = request.POST.get('age')
        clr = request.POST.get('color')
        gen = request.POST.get('gender')
        pri = request.POST.get('price')
        adrs=request.POST.get('address')
        nm = request.POST.get('name')
        phn=request.POST.get('phone')
        try:
            ptimg = request.FILES['petimg']
            fs=FileSystemStorage()
            file=fs.save(ptimg.name,ptimg)
        except MultiValueDictKeyError:
            file=sellpetdb.objects.get(id=dataid).petimg
        sellpetdb.objects.filter(id=dataid).update(pname=na,breed=brd,age=ag,color=clr,gender=gen,price=pri,address=adrs,name=nm,phone=phn,petimg=file)
        return redirect(display_sell)
def dlt_sale(request,dataid):
    data=sellpetdb.objects.filter(id=dataid)
    data.delete()
    return redirect(display_sell)
def login_seller(request):
    return render(request,"loginseller.html")
def signup_seller(request):
    return render(request,"signupseller.html")
def save_sellersignup(request):
    if request.method == "POST":
        na = request.POST.get('sname')
        pwd = request.POST.get('paswrd')
        repwd = request.POST.get('re_pswrd')
        eml = request.POST.get('email')
        phn = request.POST.get('phone')
        obj = sellersigndb(sname=na, paswrd=pwd, re_pswrd=repwd, email=eml,phone=phn)
        obj.save()
        return redirect(signup_seller)
def seller_log(request):
    if request.method=="POST":
        un=request.POST.get('sname')
        pwd=request.POST.get('paswrd')
        if sellersigndb.objects.filter(sname=un,paswrd=pwd).exists():
            request.session['sname']=un
            request.session['paswrd']=pwd
            return redirect(seller_home)
        else:
            return redirect(login_seller)
    else:
        return redirect(login_seller)