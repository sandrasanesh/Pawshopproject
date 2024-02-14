from django.urls import path
from Frontend import views
from Frontend.views import redirect_to_google_maps, redirect_to_admin_maps

urlpatterns=[
    path('home_page/',views.home_page,name="home_page"),
    path('product_page/<cat_name>/',views.product_page,name="product_page"),
    path('single_shop/<int:proid>',views.single_shop,name="single_shop"),
    path('breed_page/',views.breed_page,name="breed_page"),
    path('breed_filter/<pet_name>/',views.breed_filter,name="breed_filter"),
    path('book_pets/<int:petid>/',views.book_pets,name="book_pets"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_signup/',views.user_signup,name="user_signup"),
    path('savesignup/',views.savesignup,name="savesignup"),
    path('userlog/',views.userlog,name="userlog"),
    path('google_map/<int:dataid>/',views.google_map,name="google_map"),
    path('buypage/',views.buypage,name="buypage"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('del_cart/<int:dataid>/',views.del_cart,name="del_cart"),
    path('logout_user',views.logout_user,name="logout_user"),
    path('buy_now',views.buy_now,name="buy_now"),
    path('whislist_page/',views.whislist_page,name="whislist_page"),
    path('dlt_wishlist/<int:dataid>/',views.dlt_wishlist,name="dlt_wishlist"),
    path('user_address',views.user_address,name="user_address"),
    path('address_page',views.address_page,name="address_page"),
    path('admin_pets/<int:admid>/',views.admin_pets,name="admin_pets"),
    path('display_address/',views.display_address,name="display_address"),
    path('edit_adrs/<int:dataid>/',views.edit_adrs,name="edit_adrs"),
    path('update_address/<int:dataid>/',views.update_address,name="update_address"),
    path('dlt_adrs/<int:dataid>/',views.dlt_adrs,name="dlt_adrs"),
    path('savewishlist/',views.savewishlist,name="savewishlist"),
    # path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('reviewrating/<int:rid>/', views.reviewrating, name="reviewrating"),
    # path('review_rating/', views.review_rating, name="review_rating"),
    path('saverating/', views.saverating, name="saverating"),
    path('aboutus_page/', views.aboutus_page, name="aboutus_page"),
    path('service_page/', views.service_page, name="service_page"),
    path('sell_page/', views.sell_page, name="sell_page"),
    path('saveseller/', views.saveseller, name="saveseller"),
    path('display_sale/', views.display_sale, name="display_sale"),
    path('saleedit/<int:dataid>/', views.saleedit, name="saleedit"),
    path('sale_update/<int:dataid>/', views.sale_update, name="sale_update"),
    path('sale_dlt/<int:dataid>/', views.sale_dlt, name="sale_dlt"),
    path('product_payment/', views.product_payment, name="product_payment"),
    path('redirect-to-google-maps/<str:address>/', redirect_to_google_maps, name='redirect_to_google_maps'),
    path('redirect-to-admin-maps/<str:address>/', redirect_to_admin_maps, name='redirect_to_admin_maps'),
    path('savebuy/', views.savebuy, name="savebuy"),
    path('searchbar/', views.searchbar, name="searchbar"),
    path('notification/', views.notification, name="notification"),
    path('change_adrs/', views.change_adrs, name="change_adrs"),
    path('adminmsg/', views.adminmsg, name="adminmsg"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('savecontact/', views.savecontact, name="savecontact"),








]