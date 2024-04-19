from django.urls import path
from .views import *
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('',home, name="home"),
    path('videos', video, name = 'video'),
    path('signup',signup,name="signup"),
    path('login',handlelogin,name="handlelogin"),
    path('about/<int:product_id>',detail,name='detail'),
    path('logout', logoutfunction , name='logout'),
    path('<int:id>', detail, name='product_detail'),
    path('search', search_view, name='search'),
]