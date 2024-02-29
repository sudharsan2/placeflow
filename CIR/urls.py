from django.urls import path
from .views import enterCompanyDataAPI,getallCompanyDataAPI,handleExcelFileAPI,handleExcelStudentInfo

urlpatterns = [
    path('entercompanydata',enterCompanyDataAPI.as_view() ,name='entercompanydata'),
    path('getallcompanydata',getallCompanyDataAPI.as_view(), name='getallcompanydata' ),
    path('handleexcelRegister',handleExcelFileAPI.as_view(),name='handleexcelfile'),
    path('handleexceladdstudentdata',handleExcelStudentInfo.as_view(),name='handleexcelstudentinfo'),
    
]