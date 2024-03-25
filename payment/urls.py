from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('process/', views.PaymentProcessView.as_view(), name='payment_process'),
    path('verify/', views.PaymentVerify.as_view(), name='payment_verify'),
]
