from django.urls import path
from .views import enterCompanyDataAPI,getallCompanyDataAPI,handleExcelFileAPI,handleExcelStudentInfo,sendRegisterationTemplateAPI,UpdateCompanyDataAPI,getDepartmentAPI,getGenderAPI,getJobRoleAPI,getJobTypeAPI,getQualificationAPI,getAppliedStudentsForParticularCompany,sendStudentDataTemplateAPI,registerStudentAPI,editJob,editStudent,getastudent,getallstudents,addstudentinfo

urlpatterns = [
    path('entercompanydata',enterCompanyDataAPI.as_view() ,name='entercompanydata'),
    path('getallcompanydata',getallCompanyDataAPI.as_view(), name='getallcompanydata' ),
    path('handleexcelRegister',handleExcelFileAPI.as_view(),name='handleexcelfile'),
    path('handleexceladdstudentdata',handleExcelStudentInfo.as_view(),name='handleexcelstudentinfo'),
    path('getRegistrationTemplate',sendRegisterationTemplateAPI.as_view(), name='getregistrationtemplate' ),
    path('getStudentData',sendStudentDataTemplateAPI.as_view(),name = 'getStudentDataAPI'),
    path('updatecompanydata/<int:id>',UpdateCompanyDataAPI.as_view(),name='updatacompanydata'),
    path('getqualifications',getQualificationAPI.as_view(),name='getqualification'),
    path('getdepartments',getDepartmentAPI.as_view(),name='getdepartment'),
    path('getgenders',getGenderAPI.as_view(),name='getgender'),
    path('getjobroles',getJobRoleAPI.as_view(),name='getjobrole'),
    path('getjobtypes',getJobTypeAPI.as_view(),name='getjobtype'),
    path('getappliedstudentlist',getAppliedStudentsForParticularCompany.as_view(),name='getstudentlist'),
    path('editstudent',editStudent.as_view(),name="editstudent"),
    path('editjob',editStudent.as_view(),name="editjob"),
    path('editjob',editJob.as_view(),name="editjob"),
    path('manualregisterstudent',registerStudentAPI.as_view(), name="manualregisterstudent"),
    path('getastudent',getastudent.as_view(),name="getastudent"),
    path('getallstudents',getallstudents.as_view(),name="getalstudents"),
    path('editjob',editJob.as_view(),name="editjob"),
    path('addstudentinfo',addstudentinfo.as_view(),name="addstudentinfo"),
    # path('individualstudentregister',)


    

]