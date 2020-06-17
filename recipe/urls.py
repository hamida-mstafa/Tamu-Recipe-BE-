from django.urls import path,re_path
from . import views as views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('profile/',views.profile,name='profile'),
  path('update/',views.update_profile,name='update_profile'),
  re_path(r'^deleteaccount/$',views.deleteaccount,name='deleteaccount'),

]

if settings.DEBUG:
  urlpatterns+= static(
    settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
  )