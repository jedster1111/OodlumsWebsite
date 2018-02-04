
from django.urls import path
from . import views

app_name = 'videos'
urlpatterns = [
        path('', views.list, name = 'list'),
        path('<int:video_id>/', views.detail, name = 'detail')
    ]