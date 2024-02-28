from rest_framework import serializers
from tablemanagement.models import companyData,jobDescriptionModel,users,userRoles

class postcompanyDataSerializer(serializers.ModelSerializer):
    jobRole = serializers.ListField(write_only= True)

    class Meta:
        model = companyData
        fields = "__all__"

    def create(self, validated_data):
        job_role_data = validated_data.pop('jobRole', [])
        company_instance = super().create(validated_data)
        

        for role_name in job_role_data:
            job_description_instance,created= jobDescriptionModel.objects.get_or_create(role=role_name)
            company_instance.jobRole.add(job_description_instance)

        return company_instance
    
class jobDescriptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = jobDescriptionModel
        fields = "__all__"

class getcompanyDataSerializer(serializers.ModelSerializer):
    jobRole = jobDescriptionSerializer(many=True, required=False)

    class Meta:
        model = companyData
        fields = "__all__"


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



'''companyName = models.CharField(max_length=100)
    companyDescription = models.TextField(null = True)
    jobDescription = models.TextField(null = True)
    jobRole = models.ManyToManyField(jobDescriptionModel, null= True)
    CGPA_Required = models.FloatField(null= True)
    qualification = models.ManyToManyField(Qualification, null= True)
    eligibleDepartments = models.ManyToManyField(department, null= True)
    CTC = models.CharField(max_length = 20)
    serviceAgreement = models.CharField(max_length=30, null= True)
    trainingPeriodandStipend = models.TextField(null= True)
    workLocation = models.CharField(max_length = 100, null= True)
    evalationProcess = models.TextField(null= True) 
    jobType = models.ForeignKey(jobType, on_delete = models.CASCADE, related_name= 'jobtype',null=True)
    lastDate = models.DateField(null = True)
    markTenth = models.IntegerField(null= True)
    markTwelfth = models.IntegerField(null= True)
    maxCurrentArrears = models.ForeignKey(arrears, on_delete= models.CASCADE, related_name = "maxcurrentarrearscompany", null= True)
    historyOfArrears = models.ForeignKey(arrears, on_delete= models.CASCADE, related_name = "historyofarrearscompany", null= True)
    batch = models.IntegerField(null= True)
    '''