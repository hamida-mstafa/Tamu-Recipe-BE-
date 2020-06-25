from django.urls import path
from . import views

urlpatterns=[
    path('api/user/', views.UserList.as_view()),
    path('api/user/user-id/<username>/',views.UserDetails.as_view())
]