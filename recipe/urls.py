from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('api/user/', views.UserList.as_view()),
    path('api/user/user-id/(<pk>[0-9]+)/',
        views.UserDetails.as_view())
]