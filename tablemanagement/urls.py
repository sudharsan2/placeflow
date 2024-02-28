from django.urls import path
from .views import userRegistrationAPI,loginAPI,inserUserRoles,getUserRoles,getusers

urlpatterns = [
    path('register', userRegistrationAPI.as_view(), name='register'),
    path('login',loginAPI.as_view(), name='login' ),
    path('insert/userroles',inserUserRoles.as_view(), name= 'inserUserRole' ),
    path('getuserroles', getUserRoles.as_view(), name='getUserRole'),
    path('getusers',getusers.as_view(), name='getusers'),
]