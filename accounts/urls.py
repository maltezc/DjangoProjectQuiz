from django.conf.urls import url
from django.contrib.auth import views as auth_views
#^needed for django 1.11. imported as auth_views so that you dont mix it up with your own views
from . import views

app_name = 'accounts'


urlpatterns = [

    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$', views.SignUp.as_view(), name='signup'),

]
