from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tablemanagement.models import studentData,companyData
from .serializers import getstudentDataSerializer


class getStudentDataAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        rollNo = request.user.username
        queryset = studentData.objects.get(rollNo = rollNo)

        serializer = getstudentDataSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class getIndividualCompaniesAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        instance  = companyData.objects.get(id = id)

class applyCompaniesAPI(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request):
        payload = request.data
        rollNo = request.user.username
        instance = studentData.objects.get(rollNo = rollNo)
        company_instance = companyData.objects.get(companyName = payload.companyName)
        if (instance.CGPA>=payload.CGPA_Required and instance.gender in payload.preferredGender 
            and instance.markTenth >= payload.markTenth and instance.markTwelfth >= payload.markTenth 
            and instance.department in payload.eligibleDepartments and instance.arrear_history <= payload.historyOfArrears
            and instance.standing_Arrears <= payload.maxCurrentArrears):
            instance.appliedCompanies.add(company_instance)
            serializer = getstudentDataSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'you dont not match the requirements'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
        

''' companyName = models.CharField(max_length=100)
    websiteLink = models.CharField(max_length =255,null = True)
    preferredGender = models.ManyToManyField(gender,null=True)
    companyDescription = models.TextField(null = True)
    jobDescription = models.TextField(null = True)
    jobRole = models.ManyToManyField(jobDescriptionModel, null= True)
    CGPA_Required = models.FloatField(null= True)
    qualification = models.ManyToManyField(Qualification, null= True)
    eligibleDepartments = models.ManyToManyField(department, null= True)
    CTC = models.CharField(max_length = 20,null=True)
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
    batch = models.IntegerField(null= True)'''

"""rollNo =
    models.CharField(max_length = 50)
    department = models.ForeignKey(department, on_delete = models.CASCADE, related_name = "department")
    CGPA = models.FloatField()
    gender = models.ForeignKey(gender, on_delete = models.CASCADE, related_name = "gender")
    standing_Arrears = models.ForeignKey(arrears, on_delete = models.CASCADE, related_name = "arrears_standing")
    arrear_history = models.ForeignKey(arrears, on_delete = models.CASCADE, related_name = "arrears_history")
    markTenth = models.IntegerField(null = True)
    markTwelfth = models.IntegerField(null= True)
    # maxCurrentArrears = models.ForeignKey(arrears, on_delete= models.CASCADE, related_name = "maxcurrentarrearsstudent",null = True)
    # historyOfArrears = models.ForeignKey(arrears, on_delete= models.CASCADE, related_name = "historyofarrearsstudent",null = True)
    batch = models.IntegerField(null= True)
    appliedCompanies = models.ManyToManyField(companyData,related_name="appliedcompanies",null=True)"""