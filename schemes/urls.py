from django.urls import path
from .views import *

app_name = 'schemes'

urlpatterns = [

    #============ ADMIN APP VIEWS =============
    # Auth endpoints
    path('auth/login/', UserLoginAPIView.as_view(), name='user-login'),
    path('auth/logout/', UserLogoutAPIView.as_view(), name='user-logout'),

    # Users endpoints
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDeleteAPIView.as_view(), name='user-detail'),
    

    # Scheme endpoints
    path('schemes/', SchemeListCreateAPIView.as_view(), name='scheme-list-create'),
    path('schemes/<int:pk>/', SchemeRetrieveUpdateDeleteAPIView.as_view(), name='scheme-detail'),

    # customer endpoints

    path('customers/', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDeleteAPIView.as_view(), name='customer-detail'),

    path('customer-scheme-enrollments/', CustomerSchemeEnrollmentListCreateAPIView.as_view(), name='customer-scheme-enrollment-list-create'),

    path('customer-scheme-enrollments/<int:pk>/', CustomerSchemeEnrollmentRetrieveUpdateDeleteAPIView.as_view(), name='customer-scheme-enrollment-detail'  ),

    path('scheme-installments/',SchemeInstallmentListAPIView.as_view(), name='scheme-installment-list'),

    path('scheme-installments/<int:pk>/pay/', PayInstallmentAPIView.as_view(), name='pay-installment'),



    #============ CUSTOMER APP VIEWS =============

    path('customer/login/', CustomerLoginAPIView.as_view(), name='customer-login'),

    path('customer/logout/', CustomerLogoutAPIView.as_view(), name='customer-logout'),


    path('customer/schemes/<int:customer_id>/', CustomerSchemesAPIView.as_view(), name='customer-schemes'),
    path('customer/scheme-details/<int:enrollment_id>/', CustomerSchemeDetailAPIView.as_view(), name='customer-scheme-detail'),

    path('customer/schemes/<int:enrollment_id>/installments/', CustomerSchemeInstallmentsAPIView.as_view(), name='customer-scheme-installments'),

    path('scheme/initiate-payment/',SchemeInitiateRazorpayAPIView.as_view(),name='scheme-initiate-payment'),

    path('scheme/confirm-payment/',SchemeConfirmRazorpayAPIView.as_view(),name='scheme-verify-payment'),


    path(
        "scheme-enrollment/initiate-payment/",
        SchemeEnrollmentInitiateRazorpayAPIView.as_view(),
        name="scheme-enrollment-initiate-payment",
    ),

    path(
        "scheme-enrollment/confirm-payment/",
        SchemeEnrollmentConfirmRazorpayAPIView.as_view(),
        name="scheme-enrollment-confirm-payment",
    ),
   
    
]
