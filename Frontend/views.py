from os import name

import razorpay
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, JsonResponse

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from razorpay import Product

from Frontend.models import signupdb, cartdb, adrsdb, wishlistdb, reviewdb, sellerpetdb, buypagedb, notificationdb, \
    adminnotificationdb, contactdb
from PetsWorld import settings
from PetsWorld.settings import RAZORPAY_KEY_ID
from petsapp.models import shopdb, fooddb, catedb, petdb
from sellerapp.models import sellpetdb
from django.core.mail import send_mail, EmailMultiAlternatives


# Create your views here.
def home_page(request):
    data=shopdb.objects.all()
    pet=petdb.objects.all()

    return render(request,"home.html",{'data':data,'pet':pet})
def product_page(request, cat_name):
    # search_term = ''
    # if 'search' in request.GET:
    #     search_term = request.GET['search']
    #     data = fooddb.objects.all().filter(pname__icontains=search_term)
    data=fooddb.objects.filter(sname=cat_name)
    return render(request,"shopfilter.html",{'data':data})
def single_shop(request,proid):

    data=fooddb.objects.get(id=proid)
    return render(request,"singleshop.html",{'data':data})
def breed_page(request):
    data=catedb.objects.all()
    return render(request,"Breeds.html",{'data':data})
def breed_filter(request,pet_name):

    data=sellerpetdb.objects.filter(pname=pet_name)
    pro=petdb.objects.filter(pname=pet_name)
    return render(request,"Breedfilter.html",{'data':data,'pro':pro})
def book_pets(request,petid):
    data=sellerpetdb.objects.get(id=petid)
    pro=signupdb.objects.get(uname=request.session['uname'])

    return render(request,"bookpets.html",{'data':data,'pro':pro})
def user_login(request):
    return render(request,"userlogin.html")
def user_signup(request):
    return render(request,"usersignup.html")
def savesignup(request):
    if request.method=="POST":
        na=request.POST.get('uname')
        pwd=request.POST.get('pswrd')
        repwd=request.POST.get('re_pswrd')
        eml=request.POST.get('email')
        mob=request.POST.get('mob')
        obj=signupdb(uname=na,pswrd=pwd,re_pswrd=repwd,email=eml,mob=mob)
        obj.save()
        return redirect(user_login)
def userlog(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        pwd=request.POST.get('pswrd')
        if signupdb.objects.filter(uname=un,pswrd=pwd).exists():
            request.session['uname']=un
            request.session['pswrd']=pwd
            messages.success(request, "user logged successfully...")
            return redirect(home_page)
        else:
            messages.error(request, "user logout...")
            return redirect(user_login)
    else:
        messages.error(request, "user logout...")
        return redirect(user_login)
def google_map(request,dataid):
    data=sellerpetdb.objects.get(id=dataid)
    return render(request,"googlemap.html",{'data':data})

def redirect_to_google_maps(request, address):
    formatted_address =address.replace(' ', '+')
    google_maps_url = f"https://www.google.com/maps/search/?api=1&query={formatted_address}"
    return HttpResponseRedirect(google_maps_url)
def redirect_to_admin_maps(request, address):
    formatted_address =address.replace(' ', '+')
    google_maps_url = f"https://www.google.com/maps/search/?api=1&query={formatted_address}"
    return HttpResponseRedirect(google_maps_url)
def buypage(request):
    data=cartdb.objects.filter(uname=request.session['uname'])
    total_price=0
    for i in data:
        total_price = total_price + i.total_price
    return render(request,"billtable.html",{'data':data,'total_price':total_price})
def cart_page(request):
    if request.method=="POST":
        qty=request.POST.get('quantity')
        un=request.POST.get('uname')
        pn=request.POST.get('name')
        pri=request.POST.get('price')
        tlt=request.POST.get('total_price')
        obj=cartdb(quantity=qty,uname=un,name=pn,price=pri,total_price=tlt)
        obj.save()
        return redirect(buypage)
def del_cart(request,dataid):
    data=cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(buypage)
def logout_user(request):
    del request.session['uname']
    del request.session['pswrd']
    return redirect(userlog)
def buy_now(request):
    adrs=adrsdb.objects.filter(name=request.session['uname'])
    data = cartdb.objects.filter(uname=request.session['uname'])
    total_price = 0
    for i in data:
        total_price = total_price + i.total_price
    messages.success(request, "product added successfully...")
    return render(request,"buynow.html",{'data':data,'total_price':total_price,'adrs':adrs})

def whislist_page(request):
    data=wishlistdb.objects.filter(uname=request.session['uname'])
    return render(request,"whishlist.html",{'data':data})
def user_address(request):
    return render(request,"useraddress.html")
def address_page(request):
    if request.method=="POST":
        na=request.POST.get('name')
        mail=request.POST.get('email')
        no=request.POST.get('mob')
        house=request.POST.get('houseno')
        area=request.POST.get('area')
        land=request.POST.get('landmark')
        pin=request.POST.get('pincode')
        obj=adrsdb(name=na,email=mail,mob=no,houseno=house,area=area,landmark=land,pincode=pin)
        obj.save()
        return redirect(display_address)
def admin_pets(request,admid):
    data=petdb.objects.get(id=admid)
    pro = signupdb.objects.get(uname=request.session['uname'])
    return render(request,"adminpet.html",{'data':data,'pro':pro})

def display_address(request):
    data=adrsdb.objects.filter(name=request.session['uname'])
    return render(request,"displayaddress.html",{'data':data})
def edit_adrs(request,dataid):
    data=adrsdb.objects.get(id=dataid)
    return render(request,"editaddress.html",{'data':data})
def update_address(request,dataid):
    if request.method=="POST":
        na=request.POST.get('name')
        mail=request.POST.get('email')
        no=request.POST.get('mob')
        house=request.POST.get('houseno')
        area=request.POST.get('area')
        land=request.POST.get('landmark')
        pin=request.POST.get('pincode')
        adrsdb.objects.filter(id=dataid).update(name=na,email=mail,mob=no,houseno=house,area=area,landmark=land,pincode=pin)
        return redirect(display_address)
def dlt_adrs(request,dataid):
    data=adrsdb.objects.filter(id=dataid)
    data.delete()
    return redirect(display_address)
def savewishlist(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        pn=request.POST.get('name')
        desc=request.POST.get('des')
        pri=request.POST.get('price')
        img = request.POST.get('wishimg')
        obj=wishlistdb(uname=un,name=pn,des=desc,price=pri,wishimg=img)
        obj.save()
        return redirect(home_page)


def dlt_wishlist(request,dataid):
    wish=wishlistdb.objects.filter(id=dataid)
    wish.delete()
    return redirect(whislist_page)


#
# def add_to_wishlist(request, product_id):
#     if request.uname.is_authenticated:
#         name = get_object_or_404(wishlistdb, pk=product_id)
#
#         # Check if the item is already in the wishlist
#         if not wishlistdb.objects.filter(uname=request.session["uname"], name=name).exists():
#             wishlistdb.objects.create(uname=request.session["uname"], name=name)
#             return HttpResponse(status=200)
#         else:
#             return HttpResponse(status=400)  # Product is already in the wishlist
#     else:
#         return HttpResponse(status=401)  # Use
# def reviewrating(request,rid):
#
#     rate=reviewdb.objects.all()
#     return render(request, "review_rating.html", {'data':data,'rate':rate})

def reviewrating(request,rid):
    data = get_object_or_404(fooddb, id=rid)
    data1=reviewdb.objects.all()
    return render(request,"review_rating.html",{'data':data,'data1':data1,})

def saverating(request):
    if request.method=="POST":
        na=request.POST.get('uname')
        pro=request.POST.get('name')
        des=request.POST.get('review_des')
        rat=request.POST.get('rating')
        obj=reviewdb(uname=na,name=pro,review_des=des,rating=rat)
        obj.save()
        return redirect(home_page)
def aboutus_page(request):
    return render(request,"aboutus.html")
def service_page(request):
    return render(request,"services.html")

def sell_page(request):
    cat=catedb.objects.all()
    return render(request,"selleradd.html",{'cat':cat})
def saveseller(request):
    if request.method == "POST":
        na = request.POST.get('pname')
        brd = request.POST.get('breed')
        ag = request.POST.get('age')
        clr = request.POST.get('color')
        gen = request.POST.get('gender')
        pri = request.POST.get('price')
        adrs = request.POST.get('address')
        nm = request.POST.get('name')
        mail=request.POST.get('selleremail')
        phn = request.POST.get('phone')
        ptimg = request.FILES['petimg']
        obj = sellerpetdb(pname=na, breed=brd, age=ag, color=clr, gender=gen, price=pri, address=adrs,name=nm,selleremail=mail, phone=phn, petimg=ptimg)
        obj.save()
        return redirect(sell_page)
def display_sale(request):
    data=sellerpetdb.objects.filter(name=request.session['uname'])
    return render(request,"saledisplay.html",{'data':data})
def saleedit(request,dataid):
    data=sellerpetdb.objects.get(id=dataid)
    return render(request,"sale_edit.html",{'data':data})
def sale_update(request,dataid):
    if request.method=="POST":
        na = request.POST.get('pname')
        brd = request.POST.get('breed')
        ag = request.POST.get('age')
        clr = request.POST.get('color')
        gen = request.POST.get('gender')
        pri = request.POST.get('price')
        adrs=request.POST.get('address')
        nm = request.POST.get('name')
        mail = request.POST.get('selleremail')
        phn=request.POST.get('phone')
        try:
            ptimg = request.FILES['petimg']
            fs=FileSystemStorage()
            file=fs.save(ptimg.name,ptimg)
        except MultiValueDictKeyError:
            file=sellerpetdb.objects.get(id=dataid).petimg
        sellerpetdb.objects.filter(id=dataid).update(pname=na,breed=brd,age=ag,color=clr,gender=gen,price=pri,address=adrs,name=nm,selleremail=mail,phone=phn,petimg=file)
        return redirect(display_sale)

def sale_dlt(request, dataid):
    data = sellerpetdb.objects.filter(id=dataid)
    data.delete()
    return redirect(display_sale)

def product_payment(request):
    last_object = buypagedb.objects.order_by('-id').first()
    payy = last_object.total_price
    payy_str_product = str(payy)
    for ttpri in payy_str_product:
        print(ttpri)

    if request.method == "POST":
        amount=50000
        order_currency='INR'
        client = razorpay.Client(auth=('rzp_test_iqgFv8lRa2eIyt', 'J1Gfi6niswuxhnyqlX4SEqOC'))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
    return render(request,"payment_product.html",{'payy_str_product':payy_str_product})
def savebuy(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        fpri=request.POST.get('total_price')
        obj=buypagedb(uname=un,total_price=fpri)
        obj.save()
        return redirect(product_payment)
def searchbar(request):
    queryset = fooddb.objects.all()
    query = request.GET.get('search')
    if query:
        queryset = queryset.filter(name__icontains=query)
    context = {
        "object_list": queryset,
    }
    return render(request, "searchbar.html", context)

def notification(request):
    if request.method=='POST':
        seller=request.POST.get('selleremail')
        phn=request.POST.get('phone')
        email=request.POST.get('email')
        bred=request.POST.get('breed')
        ag=request.POST.get('age')
        pri=request.POST.get('price')
        una=request.POST.get('uname')
        mob=request.POST.get('mob')

        obj=notificationdb(selleremail=seller,phone=phn,email=email,breed=bred,age=ag,price=pri,uname=una,mob=mob)
        obj.save()
        subject = 'Interested to buy the pet'
        form_email = 'petsworld297@gmail.com'
        msg = f"hello , myself {una}. I like to buy your {bred} .You can contact me through my email {email} or phone number {mob}."
        to = seller
        msg = EmailMultiAlternatives(subject, msg, form_email,[to])
        msg.content_subtype = 'html'
        msg.send()
        return redirect(home_page)
def change_adrs(request):
    data=adrsdb.objects.filter(name=request.session['uname'])
    return render(request,"changeadrs.html",{'data':data})
def adminmsg(request):
    if request.method=='POST':
        em=request.POST.get('aemail')
        mobile=request.POST.get('amob')
        email=request.POST.get('email')
        bred=request.POST.get('breed')
        ag=request.POST.get('age')
        pri=request.POST.get('price')
        una=request.POST.get('uname')
        mob=request.POST.get('mob')
        obj=adminnotificationdb(aemail=em,amob=mobile,email=email,breed=bred,age=ag,price=pri,uname=una,mob=mob)
        obj.save()
        subject = 'Interested to buy the pet'
        form_email = 'petsworld297@gmail.com'
        msg = f"hello , myself {una}. I like to buy your {bred} .You can contact me through my email {email} or phone number {mob}."
        to = em
        msg = EmailMultiAlternatives(subject, msg, form_email,[to])
        msg.content_subtype = 'html'
        msg.send()
        return redirect(home_page)
def contact_us(request):
    return render(request,"contactus.html")
def savecontact(request):
    if request.method=='POST':
        na=request.POST.get('name')
        mail=request.POST.get('email')
        msg=request.POST.get('msg')
        obj=contactdb(name=na,email=mail,msg=msg)
        obj.save()
        return redirect(contact_us)






