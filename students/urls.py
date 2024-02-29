from django.urls import path
from .views import getStudentDataAPI,getIndividualCompaniesAPI,applyCompaniesAPI

urlpatterns =[
path('getindividualstudentdata',getStudentDataAPI.as_view(),name='getindividualstudentdata'),
path('getindividualcompaniesdata',getIndividualCompaniesAPI.as_view(),name='getindividualcompaniesdata'),
path('applycompanies',applyCompaniesAPI.as_view(),name='applycompanies')
]