from rest_framework import serializers
from CIR.serializers import genderSerializer,departmentSerializer,arrearSerializer,jobDescriptionSerializer,qualificationSerializer,jobTypeSerializer
from tablemanagement.models import studentData,companyData

# class getCompanyDataSerializer(serializers.ModelSerializer):
#     class Meta
class companyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = companyData
        fields = "__all__"
        
class getstudentDataSerializer(serializers.ModelSerializer):
    gender = genderSerializer()
    department = departmentSerializer()
    standing_Arrears = arrearSerializer()
    arrear_history = arrearSerializer()
    appliedCompanies = companyDataSerializer()

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

class addAppliesCompaniesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = studentData
        fields = "__all__"

    def create(self, validated_data):
        id = validated_data.get('id', None)
        company_instance = companyData.objects.get(id = id)
        student_instance = studentData.objects.get(rollNo = validated_data.get('rollNo', None))
        student_instance.appliedCompanies.add(company_instance)

        return student_instance
        
# class addAppliesCompaniesSerializer(serializers.ModelSerializer):
#     companyName = serializers.CharField()

#     class Meta:
#         model = studentData
#         fields = "__all__"

#     def __init__(self, *args, **kwargs):
#         # Extract and store the student_instance from kwargs
#         self.student_instance = kwargs.pop('student_instance', None)
#         super().__init__(*args, **kwargs)

#     def create(self, validated_data):
#         company_name = validated_data.get('companyName', None)
#         print(company_name)
#         company_instance = companyData.objects.get(companyName=company_name)

#         self.student_instance.appliedCompanies.add(company_instance)
#         return self.student_instance

class uploadResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentData
        fields = "__all__"