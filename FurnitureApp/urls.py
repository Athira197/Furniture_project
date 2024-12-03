from django.urls import path
from FurnitureApp import views
urlpatterns = [
    path('index/',views.index_page,name="index"),
    path('add_cat/',views.add_cat,name="add_cat"),
    path('save_cat/',views.save_cat,name="save_cat"),
    path('display_cat/',views.display_cat,name="display_cat"),
    path('edit_cat/<int:cat_id>/',views.edit_cat,name="edit_cat"),
    path('update_cat/<int:cat_id>/',views.update_cat,name="update_cat"),
    path('delete_cat/<int:cat_id>/',views.delete_cat,name="delete_cat"),

    path('add_pro/',views.add_product,name="add_pro"),
    path('save_pro/',views.save_pro,name="save_pro"),
    path('display_pro/', views.display_pro, name="display_pro"),
    path('edit_pro/<int:pro_id>/', views.edit_pro, name="edit_pro"),
    path('update_pro/<int:pro_id>/', views.update_pro, name="update_pro"),
    path('delete_pro/<int:p_id>/', views.delete_pro, name="delete_pro"),

    path('login_page/',views.login_page,name="login_page"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),

    path('contact_data/',views.contact_data,name="contact_data"),
    path('delete_contact/<int:c_id>/', views.delete_contact, name="delete_contact"),
    path('add_blog/', views.add_blog, name="add_blog"),
    path('save_blog/', views.save_blog, name="save_blog"),

]