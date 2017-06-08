from apps.views import BaseView
from apps.views import UserAuthView

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', BaseView.as_view(), name='base_view'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^user_auth/', UserAuthView.as_view(), name='user_auth'),
]
