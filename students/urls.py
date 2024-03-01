from django.urls import path
from .views import getStudentDataAPI,getIndividualCompaniesAPI,getCompanyOnCriteriaAPI,applyCompaniesAPI,uploadResumeAPI,getUploadResumeAPI

urlpatterns =[
path('getindividualstudentdata',getStudentDataAPI.as_view(),name='getindividualstudentdata'),
path('getindividualcompaniesdata',getIndividualCompaniesAPI.as_view(),name='getindividualcompaniesdata'),
path('eligiblecompanieslist',getCompanyOnCriteriaAPI.as_view(),name='eligiblecompanies'),
path('applycompany',applyCompaniesAPI.as_view(),name='applycompanies'),
path('uploadresume/<str:rollNo>',uploadResumeAPI.as_view(), name='uploadresumes'),
path('getstudentresume/<str:rollNo>',getUploadResumeAPI.as_view(), name='getresume' )
]