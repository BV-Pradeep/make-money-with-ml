from django.urls import path
from . import views

app_name='loan'

urlpatterns=[
		path('payment/', views.acceptpayments, name='payment'),
		path('predict/', views.loanform, name='predict'),
		path('approved/', views.loan_approved, name='approved'),
		path('rejected/', views.loan_rejected, name='rejected')

]