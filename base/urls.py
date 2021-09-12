from django.urls import path
from .views import PasswordDelete, PasswordList, PasswordDetail, PasswordCreate, PasswordUpdate, LoginForPassword, RegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', LoginForPassword.as_view(), name = 'login'), 
    path('register/', RegisterView.as_view(), name = 'register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', PasswordList.as_view(), name = 'list-passwords'),
    path('passwords/<int:pk>/', PasswordDetail.as_view(), name = 'detail-password'),
    path('passwords/create-password/', PasswordCreate.as_view(), name = 'create-password'),
    path('passwords-update/<int:pk>/', PasswordUpdate.as_view(), name = "update-password"),
    path('password-delete/<int:pk>/', PasswordDelete.as_view(), name = 'delete-password'),
]