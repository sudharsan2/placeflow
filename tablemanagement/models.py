from django.db import models

# Create your models here.
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **kwargs):
        
        if username is None:
            raise TypeError('User should have username')
        if email is None:
            raise TypeError('User should have email address')
        if password is None:
            raise TypeError('Password should not be empty')

        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None,  **extra_fields):

        if password is None:
            raise TypeError('Password should not be empty')

        user = self.create_user(username, email, password, **extra_fields)
        user.is_superuser = True
        user.save()
        return user
"---------------------------------------------------------------------------------------------------------------------"
class department(models.Model):
    name = models.CharField(max_length = 10)
    def __str__(self):
        return self.name
    
class gender(models.Model):
    name = models.CharField(max_length = 20)
    def __str__(self):
        return self.name
    
class arrears(models.Model):
    count = models.IntegerField()


"---------------------------------------------------------------------------------------------------------------------"
class CIRData(models.Model):
    empId = models.CharField(max_length = 20)
"---------------------------------------------------------------------------------------------------------------------"

class jobDescriptionModel(models.Model):
    role = models.CharField(max_length = 100)
    

class Qualification(models.Model):
    qualification_name = models.CharField(max_length=20)

class jobType(models.Model):
    type = models.CharField(max_length = 20)
    def __str__(self):
        return self.type

class companyData(models.Model):
    companyName = models.CharField(max_length=100)
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
    batch = models.IntegerField(null= True)

class studentData(models.Model):
    rollNo =models.CharField(max_length = 50)
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
    appliedCompanies = models.ManyToManyField(companyData,related_name="appliedcompanies",null=True)

    def __str__(self) :
        return self.rollNo
"---------------------------------------------------------------------------------------------------------------------"
class addUserExcel(models.Model):
    excelFile = models.FileField(upload_to='uploads/')

"---------------------------------------------------------------------------------------------------------------------"
class userRoles(models.Model):
    role = models.CharField(max_length =20,null=True)
    def __str__(self):
        return self.role


class users(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    username = models.CharField(max_length=255, unique=True)
    roles= models.ForeignKey(userRoles, on_delete= models.CASCADE, related_name = 'userRole')
    
    objects = UserManager() 
    
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_groups', 
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_permissions',  
        blank=True,
    )
    
    def __str__(self):
        return self.email
    
    def token(self):
        refresh_token = RefreshToken.for_user(self)
        refresh_token['username'] = self.username
        userroles = userRoles.objects.get(id=self.roles.id)
        refresh_token['role']= userroles.role
        
        return {
            'refresh_token': str(refresh_token),
            'access_token': str(refresh_token.access_token)
        }


