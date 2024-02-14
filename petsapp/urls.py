from django.urls import path
from petsapp import views
urlpatterns =[
 path('index_page/',views.index_page,name="index_page"),
 path('cate_page/',views.cate_page,name="cate_page"),
 path('savecate/',views.savecate,name="savecate"),
 path('display_cate/',views.display_cate,name="display_cate"),
 path('edit_cate/<int:dataid>/',views.edit_cate,name="edit_cate"),
 path('update_cate/<int:dataid>/',views.update_cate,name="update_cate"),
 path('dlt_cate/<int:dataid>/',views.dlt_cate,name="dlt_cate"),
 path('addpets/',views.addpets,name="addpets"),
 path('savepet/',views.savepet,name="savepet"),
 path('displaypet/',views.displaypet,name="displaypet"),
 path('edit_pets/<int:dataid>/',views.edit_pets,name="edit_pets"),
 path('update_pets/<int:dataid>/',views.update_pets,name="update_pets"),
 path('dlt_pets/<int:dataid>/',views.dlt_pets,name="dlt_pets"),
 path('add_shop/',views.add_shop,name="add_shop"),
 path('saveshop/',views.saveshop,name="saveshop"),
 path('display_shop/',views.display_shop,name="display_shop"),
 path('edit_shop/<int:dataid>/',views.edit_shop,name="edit_shop"),
 path('update_shop/<int:dataid>/',views.update_shop,name="update_shop"),
 path('delete_shop/<int:dataid>/',views.delete_shop,name="delete_shop"),
 path('add_food/',views.add_food,name="add_food"),
 path('savefood/',views.savefood,name="savefood"),
 path('displayfood/',views.displayfood,name="displayfood"),
 path('edit_food/<int:dataid>/',views.edit_food,name="edit_food"),
 path('updatefood/<int:dataid>/',views.updatefood,name="updatefood"),
 path('dlt_food/<int:dataid>/',views.dlt_food,name="dlt_food"),
 path('login_backend/',views.login_backend,name="login_backend"),
 path('loginpage/',views.loginpage,name="loginpage"),
 path('contact_display/',views.contact_display,name="contact_display"),
 path('admin_logout/',views.admin_logout,name="admin_logout"),



]
