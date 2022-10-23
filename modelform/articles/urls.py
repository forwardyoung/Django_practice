# URL 설정을 앱 단위로
from django.urls import path 
from . import views

app_name = 'articles'

urlpatterns = [
    # http://localhost:8000/articles/
    # 위 경로로 들어오면 페이지를 처리하겠다 
    path('', views.index, name='index'),
    # => views의 index라는 함수를 실행할 것이고 index라고 부를 것.
    # http://localhost:8000/articles/new/
    path('new/', views.new, name='new'),
    # http://localhost:8000/articles/create/
    path('create', views.create, name='create'),
]