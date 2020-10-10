from django.urls import path
from . import views

app_name = 'Calc'
urlpatterns =[
    path('<int:course_id>/', views.detail, name='detail'),
    path('', views.home, name='home'),
    path('<int:course_id>/yourchoice/', views.yourchoice, name='yourchoice'),


]
