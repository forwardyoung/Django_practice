from django.urls import path
from . import views # 현재 폴더 accounts에서 views를 가져오렴!

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
]