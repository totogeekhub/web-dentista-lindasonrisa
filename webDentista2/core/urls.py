#from django.contrib import admin
from django.urls import path
from .views import HomePageView, AboutPageView, StorePageView, LoginPageView, Password_change_form_PageView, AccountPageView, SignupPageView

urlpatterns = [
    #Paths del core
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('store/', StorePageView.as_view(), name="store"),
    path('login/', LoginPageView.as_view(), name="login"),
    path('signup/', SignupPageView.as_view(), name="signup"),
    path('password_change_form/', Password_change_form_PageView.as_view(), name="password_change_form"),
    path('account/', AccountPageView.as_view(), name="account"),
]