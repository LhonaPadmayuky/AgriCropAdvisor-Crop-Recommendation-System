from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict_crop/', views.predict_crop, name='predict_crop'),
    path('recommend_crop/', views.recommend_crop, name='recommend_crop'),
    path('about/', views.about, name='about'), 
    path('crops/', views.crops, name='crops'),  
]
