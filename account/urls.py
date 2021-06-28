from django.urls import path

from . import views
urlpatterns=[
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('cart',views.cart,name="cart"),
    path('order1',views.order1,name="order1"),
    path('home',views.home,name="home"),
    path('final',views.final,name="final"),
    path('download',views.download,name='download')
    

]