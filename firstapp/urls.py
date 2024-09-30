from django.urls import path, include
from .views import RegisterView, LoginView, LogoutView, TokenVerifyView, ProductView, AllProductsView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify/', TokenVerifyView.as_view(), name='verify'),
    path('product/<slug:slug>/', ProductView.as_view(), name='product'),
    path('allproducts/', AllProductsView.as_view(), name='allproducts')
]
