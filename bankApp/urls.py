from django.urls import path
from . import views

urlpatterns = [
path('', views.upload, name='home'),
path('accounts', views.accounts, name='accounts'),
path('transaction', views.transaction, name='transaction'),
]