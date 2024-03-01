from django.urls import path
from .views import getStudentDataAPI,getIndividualCompaniesAPI,getCompanyOnCriteriaAPI,applyCompaniesAPI

urlpatterns =[
path('getindividualstudentdata',getStudentDataAPI.as_view(),name='getindividualstudentdata'),
path('getindividualcompaniesdata',getIndividualCompaniesAPI.as_view(),name='getindividualcompaniesdata'),
path('eligiblecompanieslist',getCompanyOnCriteriaAPI.as_view(),name='eligiblecompanies'),
path('applycompany',applyCompaniesAPI.as_view(),name='applycompanies')
]