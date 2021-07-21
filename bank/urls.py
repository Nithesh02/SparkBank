from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_view, name='index'), 
    path('new_customer/',views.new_customer, name='new_customer'), 
    path('view_customers/',views.view_customers, name='view_customers'), 
    path('customer_details/<str:pk>/',views.customer_details, name='customer_details'), 
]