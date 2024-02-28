from django.urls import path
from .views import enterCompanyDataAPI,getallCompanyDataAPI,handleExcelFileAPI

urlpatterns = [
    path('entercompanydata',enterCompanyDataAPI.as_view() ,name='entercompanydata'),
    path('getallcompanydata',getallCompanyDataAPI.as_view(), name='getallcompanydata' ),
    path('handleexcel',handleExcelFileAPI.as_view(),name='handleexcelfile')
]