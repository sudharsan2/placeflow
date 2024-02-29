from rest_framework import serializers
from CIR.serializers import genderSerializer,departmentSerializer,arrearSerializer,jobDescriptionSerializer,qualificationSerializer,jobTypeSerializer
from tablemanagement.models import studentData,companyData

class getstudentDataSerializer(serializers.ModelSerializer):
    gender = genderSerializer()
    department = departmentSerializer()
    standing_Arrears = arrearSerializer()
    arrear_history = arrearSerializer()

    class Meta:
        model = studentData
        fields = "__all__"

class getStudentSpecificCompanySerializer(serializers.ModelSerializer):
    jobRole = jobDescriptionSerializer(many=True, required=False)
    preferredGender = genderSerializer(many= True)
    qualification = qualificationSerializer(many= True)
    eligibleDepartments = departmentSerializer(many= True)
    jobType = jobTypeSerializer()
    maxCurrentArrears = arrearSerializer()
    historyOfArrears = arrearSerializer()

    class Meta:
        model = companyData
        fields = "__all__"