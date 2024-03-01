from django.urls import path
from .views import enterCompanyDataAPI,getallCompanyDataAPI,handleExcelFileAPI,handleExcelStudentInfo,sendRegisterationTemplateAPI,UpdateCompanyDataAPI,getDepartmentAPI,getGenderAPI,getJobRoleAPI,getJobTypeAPI,getQualificationAPI,getAppliedStudentsForParticularCompany

urlpatterns = [
    path('entercompanydata',enterCompanyDataAPI.as_view() ,name='entercompanydata'),
    path('getallcompanydata',getallCompanyDataAPI.as_view(), name='getallcompanydata' ),
    path('handleexcelRegister',handleExcelFileAPI.as_view(),name='handleexcelfile'),
    path('handleexceladdstudentdata',handleExcelStudentInfo.as_view(),name='handleexcelstudentinfo'),
    path('getRegistrationTemplate',sendRegisterationTemplateAPI.as_view(), name='getregistrationtemplate' ),
    path('updatecompanydata/<int:id>',UpdateCompanyDataAPI.as_view(),name='updatacompanydata'),
    path('getqualifications',getQualificationAPI.as_view(),name='getqualification'),
    path('getdepartments',getDepartmentAPI.as_view(),name='getdepartment'),
    path('getgenders',getGenderAPI.as_view(),name='getgender'),
    path('getjobroles',getJobRoleAPI.as_view(),name='getjobrole'),
    path('getjobtypes',getJobTypeAPI.as_view(),name='getjobtype'),
    path('getappliedstudentlist',getAppliedStudentsForParticularCompany.as_view(),name='getstudentlist'),


    

]