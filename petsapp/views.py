from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from Frontend.models import contactdb
from Frontend.views import user_address
from petsapp.models import catedb, petdb, shopdb, fooddb


# Create your views here.
def index_page(request):
    return render(request,"index.html")
def cate_page(request):
    cat=catedb.objects.all()
    return render(request,"addcategory.html",{'cat':cat})
def savecate(request):
    if request.method=="POST":
        name=request.POST.get('pname')
        des=request.POST.get('pdes')
        img=request.FILES['pimg']
        obj=catedb(pname=name,pdes=des,pimg=img)
        obj.save()
        return redirect(cate_page)
def display_cate(request):
    data=catedb.objects.all()
    return render(request,"displaycate.html",{'data':data})
def edit_cate(request,dataid):
    data=catedb.objects.get(id=dataid)
    return render(request,"editcate.html",{'data':data})
def update_cate(request,dataid):
    if request.method=="POST":
        name = request.POST.get('pname')
        des = request.POST.get('pdes')
        try:
            img = request.FILES['pimg']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=catedb.objects.get(id=dataid).pimg
        catedb.objects.filter(id=dataid).update(pname=name,pdes=des,pimg=file)
        return redirect(display_cate)
def dlt_cate(request,dataid):
    data=catedb.objects.filter(id=dataid)
    data.delete()
    return redirect(display_cate)
def addpets(request):
    data=catedb.objects.all()
    return render(request,"addpets.html",{'data':data})
def savepet(request):
    if request.method=="POST":
        na=request.POST.get('pname')
        brd=request.POST.get('breed')
        ag=request.POST.get('age')
        clr=request.POST.get('color')
        gen=request.POST.get('gender')
        pri=request.POST.get('price')
        adrs=request.POST.get('address')
        name=request.POST.get('aname')
        email=request.POST.get('aemail')
        mob=request.POST.get('amob')

        ptimg=request.FILES['petimg']
        obj=petdb(pname=na,breed=brd,age=ag,color=clr,gender=gen,price=pri,address=adrs,aname=name,aemail=email,amob=mob,petimg=ptimg)
        obj.save()
        return redirect(addpets)
def displaypet(request):
    data=petdb.objects.all()
    return render(request,"displaypets.html",{'data':data})
def edit_pets(request,dataid):
    data=petdb.objects.get(id=dataid)
    return render(request,"editpets.html",{'data':data})
def update_pets(request,dataid):
    if request.method=="POST":
        na = request.POST.get('pname')
        brd = request.POST.get('breed')
        ag = request.POST.get('age')
        clr = request.POST.get('color')
        gen = request.POST.get('gender')
        pri = request.POST.get('price')
        adrs=request.POST.get('address')

        try:
            ptimg = request.FILES['petimg']
            fs=FileSystemStorage()
            file=fs.save(ptimg.name,ptimg)
        except MultiValueDictKeyError:
            file=petdb.objects.get(id=dataid).petimg
        petdb.objects.filter(id=dataid).update(pname=na,breed=brd,age=ag,color=clr,gender=gen,price=pri,address=adrs,petimg=file)
        return redirect(displaypet)
def dlt_pets(request,dataid):
    data=petdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaypet)
def add_shop(request):
    data=shopdb.objects.all()
    return render(request,"add shops.html",{'data':data})
def saveshop(request):
    if request.method=="POST":
        na=request.POST.get('sname')
        img=request.FILES['simg']
        obj=shopdb(sname=na,simg=img)
        obj.save()
        return redirect(add_shop)
def display_shop(request):
    data=shopdb.objects.all()
    return render(request,"displayshop.html",{'data':data})
def edit_shop(request,dataid):
    data=shopdb.objects.get(id=dataid)
    return render(request,"editshop.html",{'data':data})
def update_shop(request,dataid):
    if request.method=="POST":
        na = request.POST.get('sname')
        try:
            img = request.FILES['simg']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=shopdb.objects.get(id=dataid).simg
        shopdb.objects.filter(id=dataid).update(sname=na,simg=file)
        return redirect(display_shop)
def delete_shop(request,dataid):
    data=shopdb.objects.filter(id=dataid)
    data.delete()
    return redirect(display_shop)
def add_food(request):
    shop=shopdb.objects.all()
    data=catedb.objects.all()
    return render(request,"addfood.html",{'data':data,'shop':shop})
def savefood(request):
    if request.method=="POST":
        pn=request.POST.get('pname')
        sn=request.POST.get('sname')
        na=request.POST.get('name')
        de=request.POST.get('des')
        pri=request.POST.get('price')
        img=request.FILES['fimg']
        obj=fooddb(pname=pn,sname=sn,name=na,des=de,price=pri,fimg=img)
        obj.save()
        return redirect(add_food)
def displayfood(request):
    data=fooddb.objects.all()
    return render(request,"displayfood.html",{'data':data})
def edit_food(request,dataid):
    data=fooddb.objects.get(id=dataid)
    cat=catedb.objects.all()
    shop=shopdb.objects.all()
    return render(request,"editfood.html",{'data':data,'cat':cat,'shop':shop})
def updatefood(request,dataid):
    if request.method=="POST":
        pn=request.POST.get('pname')
        sn=request.POST.get('sname')
        na=request.POST.get('name')
        de=request.POST.get('des')
        pri=request.POST.get('price')

        try:
            img = request.FILES['fimg']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=fooddb.objects.get(id=dataid).fimg
        fooddb.objects.filter(id=dataid).update(pname=pn,sname=sn,name=na,des=de,price=pri,fimg=file)
        return redirect(displayfood)
def dlt_food(request,dataid):
    data=fooddb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayfood)
def login_backend(request):
    return render(request,"loginbackend.html")


def loginpage(request):
    if request.method=='POST':
        un=request.POST.get('user_name')
        pwd=request.POST.get('pass_word')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                return redirect(index_page)
            else:
                return redirect(login_backend)

        else:
            return redirect(login_backend)
def contact_display(request):
    data=contactdb.objects.all()
    return render(request,"displaycontact.html",{'data':data})
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_backend)







