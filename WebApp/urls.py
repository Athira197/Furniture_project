from django.urls import path
from WebApp import views
urlpatterns = [
    path('home/',views.home_page,name="home"),
    path('product_page/',views.product_page,name="product_page"),
    path('about_page/',views.about_page,name="about_page"),
    path('contact_page/',views.contact_page,name="contact_page"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('filter_products/<cat_name>/',views.filter_products,name="filter_products"),
    path('single_product/<int:pro_id>/',views.single_product,name="single_product"),
    path('blog_page/',views.blog_page,name="blog_page"),
    path('register/',views.register,name="register"),
    path('',views.login_page,name="login_page"),
    path('save_register/',views.save_register,name="save_register"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/',views.user_logout,name="user_logout"),


    path('save_cart/',views.save_cart,name="save_cart"),
    path('cart/',views.cart,name="cart"),
    path('delete_cart/<int:cart_id>/',views.delete_cart,name="delete_cart"),
    path("checkout/",views.checkout,name="checkout"),
    path("save_checkout/",views.save_checkout,name="save_checkout"),
    path("payment/",views.payment,name="payment"),

]