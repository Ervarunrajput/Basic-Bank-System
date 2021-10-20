from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = "index"),
    path('customers',views.customers,name = "customers"),
    path('transactions',views.transactions,name = "transactions"),
    path('transfer/<event_id>',views.transfer,name = "transfer"),
    path('process/<event_id>',views.process,name = "process"),
]
