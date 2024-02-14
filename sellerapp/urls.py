from django.urls import path
from sellerapp import views
urlpatterns =[
    path('seller_home/',views.seller_home,name="seller_home"),
    path('seller_pets/',views.seller_pets,name="seller_pets"),
    path('savesell/',views.savesell,name="savesell"),
    path('display_sell/',views.display_sell,name="display_sell"),
    path('edit_sale/<int:dataid>/',views.edit_sale,name="edit_sale"),

    path('update_sale/<int:dataid>/',views.update_sale,name="update_sale"),
    path('dlt_sale/<int:dataid>/',views.dlt_sale,name="dlt_sale"),
    path('login_seller/',views.login_seller,name="login_seller"),
    path('signup_seller/',views.signup_seller,name="signup_seller"),
    path('save_sellersignup/',views.save_sellersignup,name="save_sellersignup"),
    path('seller_log/',views.seller_log,name="seller_log"),

]