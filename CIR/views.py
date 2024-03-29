from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import postcompanyDataSerializer,excelRegistrationSerializer,excelAddStudentInfoSerializer,qualificationSerializer,departmentSerializer,jobTypeSerializer,jobDescriptionSerializer,genderSerializer,PatchCompanyDataSerializer,studentDataSerializer,getCompanyDataSerializer
from tablemanagement.models import companyData,studentData,Qualification,department,jobType,jobDescriptionModel,gender
from students.serializers import getstudentDataSerializer,companyDataSerializer
from .appliedstudents import write_dict_to_excel
from rest_framework.response import Response
from django.http import FileResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import base64
from django.http import HttpRequest,HttpResponse
import pandas as pd
import requests
from io import BytesIO
from django.conf import settings
import base64
import openpyxl
import os
# from django.http import HttpResponse


class enterCompanyDataAPI(APIView):
    def post(self, request):
        try:
            payload = request.data
            serializer = postcompanyDataSerializer(data=payload)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message":"Successfully Inserted the Data"}, status=status.HTTP_201_CREATED)


class getallCompanyDataAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            payload = companyData.objects.all()
            serializer = getCompanyDataSerializer(payload, many= True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class getacompanyDataAPI(APIView):
    def get(self, request, **kwargs):
        try:
            id = kwargs.get('id')
            payload = companyData.objects.get(id = id)
            serializer = getCompanyDataSerializer(payload)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
class registerStudentAPI(APIView):
    permission_classes= [IsAuthenticated]
    def post(self,request):

        request_data = {"username": request.data.get("username"),
                            "password": request.data.get("username")+request.data.get("dob"), 
                            "dob" : request.data.get("dob"),
                            "email": request.data.get("email"),
                            "roles": "student"}  
            
        serializer = excelRegistrationSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            
        return Response("successfully user created", status=status.HTTP_201_CREATED)

        
class handleExcelFileAPI(APIView):
    permission_classes= [IsAuthenticated]
    def post(self, request):
        payload = request.data['excel']
        file_content = payload.read()
        excelFile = BytesIO(file_content)

        df = pd.read_excel(excelFile, header=None)
        # Extract column names from row 3
        columns = df.iloc[0].tolist()
        # Extract data starting from row 4
        data = df.iloc[1:]
        # Reset index to make it easier to work with
        data = data.reset_index(drop=True)
        # Create a list of dictionaries using column names and corresponding row values
        result_list = [dict(zip(columns, row)) for index, row in data.iterrows()]
        responses = []

        for data_dict in result_list:
            
            request_data = {"username": data_dict["username"], 
                            "dob" : data_dict["dob"],
                            "password": "welcome", 
                            "email": data_dict["username"]+"@gmail.com",
                            "roles": "student"}  
            
            serializer = excelRegistrationSerializer(data=request_data)
            if serializer.is_valid():
                serializer.save()
                responses.append(serializer.data)
        return Response(responses, status=status.HTTP_201_CREATED)
    
class addstudentinfo(APIView):
    def post(self, request):
        try:
            request_data = {"rollNo": request.data.get("rollno",None), 
                                        "department": request.data.get("department",None), 
                                        "CGPA": float(request.data.get("cgpa",None)),
                                        "gender": request.data.get("gender",None), 
                                        "standing_Arrears": int(request.data.get("standing_arrears",None)),
                                        "arrear_history": int(request.data.get("arrear_history",None)), 
                                        "markTenth": int(request.data.get("Tenth_mark",None)),
                                        "markTwelfth": int(request.data.get("Twelfth_mark",None)),
                                        "batch": int(request.data.get("batch",None)),
                                        "appliedCompanies" : None}
            serializer = excelAddStudentInfoSerializer(data=request_data)
            if serializer.is_valid():
                serializer.save()
                
            return Response(request_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": "Data Inserted Successfully"},status=status.HTTP_201_CREATED)

class handleExcelStudentInfo(APIView):
    # permission_classes= [IsAuthenticated]
    def post(self, request):
            try:
                payload = request.data['excel']
                file_content = payload.read()
                excel_file = BytesIO(file_content)
                df = pd.read_excel(excel_file, header=None)
                columns = df.iloc[0].tolist()
                data = df.iloc[1:]
                data = data.reset_index(drop=True)
                result_list = [dict(zip(columns, row))for index,row in data.iterrows()]

                responses =[]
                for data_dict in result_list:
                    request_data = {"rollNo": data_dict["rollno"], 
                                    "department": data_dict["department"], 
                                    "CGPA": float(data_dict["cgpa"]),
                                    "gender": data_dict["gender"], 
                                    "standing_Arrears": int(data_dict["standing_arrears"]),
                                    "arrear_history": int(data_dict["arrear_history"]), 
                                    "markTenth": int(data_dict["Tenth_mark"]),
                                    "markTwelfth": int(data_dict["Twelfth_mark"]),
                                    "batch": int(data_dict["batch"]),
                                    "appliedCompanies" : None}
                    serializer = excelAddStudentInfoSerializer(data=request_data)
                    if serializer.is_valid():
                        serializer.save()
                        responses.append(serializer.data)
                return Response(responses, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"message": "Data Inserted Successfully"},status=status.HTTP_201_CREATED)
            

        
class sendRegisterationTemplateAPI(APIView):
    def get(self, request):
        file_path =  (settings.BASE_DIR / "ExcelTemplate/Book10.xlsx").resolve()

        with open(file_path,'rb') as excel_file:            
# Create BytesIO object
            excel_bytes = BytesIO(excel_file.read())        
# Create response
        response = HttpResponse(excel_bytes, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] ='attachment; filename="registerTemplate.xlsx"'
        return response
    

    
class sendStudentDataTemplateAPI(APIView):
    def get(self, request):
        file_path =  (settings.BASE_DIR / "ExcelTemplate/Book11.xlsx").resolve()

        with open(file_path,'rb') as excel_file:            
# Create BytesIO object
            excel_bytes = BytesIO(excel_file.read())        
# Create response
        response = HttpResponse(excel_bytes, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] ='attachment; filename="registerTemplate.xlsx"'
        return response
        


class getQualificationAPI(APIView):
    def get(self, request):
        instance = Qualification.objects.all()
        serializer = qualificationSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class getDepartmentAPI(APIView):
    def get(self, request):
        instance = department.objects.all()
        serializer = departmentSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class getJobTypeAPI(APIView):
    def get(self, request):
        instance = jobType.objects.all()
        serializer = jobTypeSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class getJobRoleAPI(APIView):
    def get(self, request):
        instance = jobDescriptionModel.objects.all()
        serializer = jobDescriptionSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class getGenderAPI(APIView):
    def get(self, request):
        instance = gender.objects.all()
        serializer = genderSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UpdateCompanyDataAPI(APIView):
    def patch(self, request, **kwargs):
        try:
            payload = request.data
            id = kwargs.get('id')
            instance = companyData.objects.get(id = id)
            serializer = PatchCompanyDataSerializer(instance, data=payload, partial= True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
        except Exception as e:
            return Response({"message":"Data Updated Successfully"}, status=status.HTTP_206_PARTIAL_CONTENT)




# class getAppliedStudentsForParticularCompany(APIView):
    
#     def post(self,request):
#         payload = request.data
#         jobPostId = payload.get('id',None)
#         student_instance = studentData.objects.all()
#         serializer2 = studentDataSerializer(student_instance, many = True)
#         studentrollnolist =[]
#         studentresumelist =[]
#         data2 = serializer2.data
#         existing_excel_file = (settings.BASE_DIR / "ExcelTemplate/appliedStudents.xlsx").resolve()
#         target_column1 = "applied Students"
#         target_column2 = "resumes"
        
        

        
#         for i in data2:
#             if jobPostId in i['appliedCompanies']:
#                 studentrollnolist.append(i['rollNo'])
#                 studentresumelist.append(f"http://127.0.0.1:8000/students/getstudentresume/{i['rollNo']}")
#         if len(studentrollnolist) !=0 :
#             write_list_to_excel(existing_excel_file, target_column1, studentrollnolist)
#         else: 
#             write_list_to_excel(existing_excel_file, target_column1, ["no one applies yet"])

#         with open(existing_excel_file,'rb') as file:
#             excel_bytes = BytesIO(file.read()) 
#         response = HttpResponse(excel_bytes, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#         response['Content-Disposition'] ='attachment; filename="appliedStudentsList.xlsx"'
#         return response

class getAppliedStudentsForParticularCompany(APIView):
    
    def post(self, request):
        payload = request.data
        jobPostId = payload.get('id', None)
        student_instance = studentData.objects.all()
        serializer2 = studentDataSerializer(student_instance, many=True)
        data2 = serializer2.data

        existing_excel_file = (settings.BASE_DIR / "ExcelTemplate/appliedStudents.xlsx").resolve()
        new_excel_file = (settings.BASE_DIR / "appliedStudent.xlsx").resolve()
        target_columns = {
            "applied Students": [],
            "resumes": [],
            # Add more columns as needed
        }

        for i in data2:
            if jobPostId in i['appliedCompanies']:
                target_columns["applied Students"].append(i['rollNo'])
                target_columns["resumes"].append(f"http://127.0.0.1:8000/students/getstudentresume/{i['rollNo']}")
                # Add more columns as needed

        if any(target_columns.values()):
            write_dict_to_excel(existing_excel_file, target_columns)
        else: 
            write_dict_to_excel(existing_excel_file, {"applied_students": ["no one applies yet"]})

        with open(existing_excel_file, 'rb') as file:
            excel_bytes = BytesIO(file.read()) 

        response = HttpResponse(new_excel_file, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="appliedStudentsList.xlsx"'
        return response
    

class getallstudents(APIView):
    def get(self, request):
        instance = studentData.objects.all()
        serializer = studentDataSerializer(instance, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Example usage

class getastudent(APIView):
    def get(self, request,**kwargs):
        id = kwargs.get('id')
        instance = studentData.objects.get(id = id)
        serializer = studentDataSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class editStudent(APIView):
    def post(self, request):
        id = request.data['id']
        instance = studentData.objects.get(id = id)
        serializer = studentDataSerializer(instance,data = request.data ,partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class editJob(APIView):
    def post(self, request):
        id = request.data['id']
        instance = companyData.objects.get(id = id)
        serializer = companyDataSerializer(instance, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)