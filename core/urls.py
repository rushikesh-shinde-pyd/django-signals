from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index_view, name='homepage'),
    path('signup/', views.signup_view, name='signup'),

]