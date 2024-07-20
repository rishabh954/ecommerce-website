"""
URL configuration for ecomerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index.html"),
    path('404.html', views.four, name="404.html"),
    path('cart.html', views.cart, name="cart.html"),
    path('chackout.html', views.chackout, name="chackout.html"),
    path('contact.html', views.contact, name="contact.html"),
    path('shop-detail.html', views.shop_detail, name="shop-detail.html"),
    path('shop.html', views.shop, name="shop.html"),
    path('testimonial.html', views.test, name="testimonial.html"),
    path('register',views.registration,name="register"),
    path('fetchregister',views.fetchregister,name="fetchregister"),
    path('login',views.login,name="login"),
    path('fetchlogin',views.fetchlogin,name="fetchlogindata"),
    path('logout',views.logout,name="logout"),
    path('forgot',views.forgot,name="forgot"),
    path('forgot-password',views.forgotpassword,name="forgot-password")
]
