from rest_framework import serializers
from tablemanagement.models import companyData,jobDescriptionModel,users,userRoles,studentData,department,gender,arrears,Qualification,jobType




class postcompanyDataSerializer(serializers.ModelSerializer):
    jobRole = serializers.ListField(write_only=True)
    preferredGender = serializers.ListField(write_only=True)
    qualification = serializers.ListField(write_only=True)
    eligibleDepartments = serializers.ListField(write_only=True)
    jobType = serializers.CharField(required=False)
    maxCurrentArrears = serializers.IntegerField(required=False)
    historyOfArrears = serializers.IntegerField(required=False)

    class Meta:
        model = companyData  
        fields = ["companyName","companyDescription",
    "preferredGender" ,
    "jobDescription",
    "jobRole",
    "jobType",
    "qualification",
    "eligibleDepartments",
    "lastDate",
    "markTenth",
    "markTwelfth",
    "maxCurrentArrears",
    "historyOfArrears",
    "CGPA_Required",
    "batch",
    "CTC",
    "serviceAgreement",
    "trainingPeriodandStipend",
    "workLocation",
    "evalationProcess"]

    def create(self, validated_data):
        job_role_data = validated_data.pop('jobRole', [])
        gender_data = validated_data.pop('preferredGender', [])
        qualification_data = validated_data.pop('qualification', [])
        department_data = validated_data.pop('eligibleDepartments', [])
        jobtype_data = validated_data.pop('jobType', '')
        currentarrear_data = validated_data.pop('maxCurrentArrears', 0)
        arrearhistory_data = validated_data.pop('historyOfArrears', 0)
        print(validated_data)

        jobtype_instance, _ = jobType.objects.get_or_create(type=jobtype_data)
        currentarrear_instance, _ = arrears.objects.get_or_create(count=currentarrear_data)
        arrearhistory_instance, _ = arrears.objects.get_or_create(count=arrearhistory_data)

        validated_data['jobType'] = jobtype_instance
        validated_data['maxCurrentArrears'] = currentarrear_instance
        validated_data['historyOfArrears'] = arrearhistory_instance

        print(validated_data)
        

        company_instance = companyData.objects.create(**validated_data)

        # Add the related objects
        for role_name in job_role_data:
            job_description_instance1, created1 = jobDescriptionModel.objects.get_or_create(role=role_name)
            company_instance.jobRole.add(job_description_instance1)

        for role_name in gender_data:
            job_description_instance2, created2 = gender.objects.get_or_create(name=role_name)
            company_instance.preferredGender.add(job_description_instance2)

        for role_name in qualification_data:
            job_description_instance3, created3 = Qualification.objects.get_or_create(qualification_name=role_name)
            company_instance.qualification.add(job_description_instance3)

        for role_name in department_data:
            job_description_instance4, created4 = department.objects.get_or_create(name=role_name)
            company_instance.eligibleDepartments.add(job_description_instance4)

        return company_instance

from rest_framework import serializers

class PatchCompanyDataSerializer(serializers.Serializer):
    jobRole = serializers.ListField(write_only=True)
    preferredGender = serializers.ListField(write_only=True)
    qualification = serializers.ListField(write_only=True)
    eligibleDepartments = serializers.ListField(write_only=True)
    jobType = serializers.CharField(required=False)
    maxCurrentArrears = serializers.IntegerField(required=False)
    historyOfArrears = serializers.IntegerField(required=False)

    def update(self, instance, validated_data):
        job_role_data = validated_data.pop('jobRole', [])
        gender_data = validated_data.pop('preferredGender', [])
        qualification_data = validated_data.pop('qualification', [])
        department_data = validated_data.pop('eligibleDepartments', [])
        jobtype_data = validated_data.pop('jobType', '')
        currentarrear_data = validated_data.pop('maxCurrentArrears', 0)
        arrearhistory_data = validated_data.pop('historyOfArrears', 0)

        jobtype_instance, _ = jobType.objects.get_or_create(type=jobtype_data)
        currentarrear_instance, _ = arrears.objects.get_or_create(count=currentarrear_data)
        arrearhistory_instance, _ = arrears.objects.get_or_create(count=arrearhistory_data)

        validated_data['jobType'] = jobtype_instance
        validated_data['maxCurrentArrears'] = currentarrear_instance
        validated_data['historyOfArrears'] = arrearhistory_instance

        # Update the instance with the remaining validated_data
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        # Update the related objects
        instance.jobRole.clear()
        for role_name in job_role_data:
            job_description_instance1, created1 = jobDescriptionModel.objects.get_or_create(role=role_name)
            instance.jobRole.add(job_description_instance1)

        instance.preferredGender.clear()
        for role_name in gender_data:
            job_description_instance2, created2 = gender.objects.get_or_create(name=role_name)
            instance.preferredGender.add(job_description_instance2)

        instance.qualification.clear()
        for role_name in qualification_data:
            job_description_instance3, created3 = Qualification.objects.get_or_create(qualification_name=role_name)
            instance.qualification.add(job_description_instance3)

        instance.eligibleDepartments.clear()
        for role_name in department_data:
            job_description_instance4, created4 = department.objects.get_or_create(name=role_name)
            instance.eligibleDepartments.add(job_description_instance4)

        return instance


class jobDescriptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = jobDescriptionModel
        fields = "__all__"

class genderSerializer(serializers.ModelSerializer):
    class Meta:
        model = gender
        fields = "__all__"

class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = "__all__"

class arrearSerializer(serializers.ModelSerializer):
    class Meta:
        model = arrears
        fields = "__all__"

class qualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = "__all__"

class jobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobType
        fields = "__all__"

class companyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = companyData
        fields = "__all__"
        

class studentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentData
        fields = "__all__"



'''
    preferredGender = models.ManyToManyField(gender,null=True)
    jobRole = models.ManyToManyField(jobDescriptionModel, null= True)
    qualification = models.ManyToManyField(Qualification, null= True)
    eligibleDepartments = models.ManyToManyField(department, null= True)
    jobType = models.ForeignKey(jobType, on_delete = models.CASCADE, related_name= 'jobtype',null=True)
    maxCurrentArrears = models.ForeignKey(arrears, on_delete= models.CASCADE, related_name = "maxcurrentarrearscompany", null= True)
    historyOfArrears = models.ForeignKey(arrears, on_delete= models.CASCADE, related_name = "historyofarrearscompany", null= True)
'''


class excelRegistrationSerializer(serializers.ModelSerializer):
    roles = serializers.CharField(max_length= 20)
    password = serializers.CharField(max_length=255, write_only = True)

    class Meta:
        model = users
        fields = ['username', 'email', 'password', 'roles']

    def create(self, validated_data):

        role_data = validated_data.get('roles','')
        role_instance,created = userRoles.objects.get_or_create(role = role_data)
        validated_data['roles'] = role_instance
        # validated_data['password'] = "welcome"
        return users.objects.create_user(**validated_data)
    


class excelAddStudentInfoSerializer(serializers.ModelSerializer):
    department = serializers.CharField(max_length=10)
    gender = serializers.CharField(max_length=10)
    standing_Arrears = serializers.IntegerField()
    arrear_history = serializers.IntegerField()

    class Meta:
        model = studentData
        fields = "__all__"

    def create(self, validated_data):
        departments = validated_data.get('department', '')
        genders = validated_data.get('gender', '')
        standing_arrears_value = validated_data.pop('standing_Arrears', None)
        arrear_history_value = validated_data.pop('arrear_history', None)

        

        department_instance, created = department.objects.get_or_create(name=departments)
        gender_instance, created = gender.objects.get_or_create(name=genders)

        standing_arrears_instance, _ = arrears.objects.get_or_create(count=standing_arrears_value)
        arrear_history_instance, _ = arrears.objects.get_or_create(count=arrear_history_value)

        validated_data['department'] = department_instance
        validated_data['gender'] = gender_instance
        validated_data['standing_Arrears'] = standing_arrears_instance
        validated_data['arrear_history'] = arrear_history_instance

        return studentData.objects.create(**validated_data)

class genderSerializer(serializers.ModelSerializer):
    class Meta:
        model = gender
        fields = "__all__"

class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = "__all__"

class arrearSerializer(serializers.ModelSerializer):
    class Meta:
        model = arrears
        fields = "__all__"

# class getAppliesStudentsListSerializer(serializers.Serializer):
#     id = serializers.IntegerField()

#     def create(self, validated_data):
#         id = validated_data.get('id',None)
#         company_instance = companyData.objects.get(id=id)
#         c



