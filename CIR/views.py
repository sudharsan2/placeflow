from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import postcompanyDataSerializer,getcompanyDataSerializer,excelRegistrationSerializer,excelAddStudentInfoSerializer
from tablemanagement.models import companyData,studentData
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
            serializer = getcompanyDataSerializer(payload, many= True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

        
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
                            "password": "welcome", 
                            "email": data_dict["username"]+"@gmail.com",
                            "roles": "student"}  
            
            serializer = excelRegistrationSerializer(data=request_data)
            if serializer.is_valid():
                serializer.save()
                responses.append(serializer.data)
        return Response(responses, status=status.HTTP_201_CREATED)
    

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
        # with open(file_path,'rb') as file:
        #     file_content = file.read()

        # # base64_content = base64.b64encode(file_content).decode('utf-8')
        # meta_data = {
        #     "file_name" : "Registeration Template",
        #     "file_size" : len(file_content)
        # }

        # response_data = {
        #     # "metadata" : meta_data,
        #     "Template" : file_content
        # }

        # return FileResponse(file_content, as_attachment=True, filename="Registration_Template.xlsx")
        # df = pd.read_excel(file_path)

        #         # Convert DataFrame to blob
        # excel_data = BytesIO()
        # with pd.ExcelWriter(excel_data, engine='xlsxwriter') as writer:
        #     df.to_excel(writer, index=False)
        # excel_data.seek(0)
        # Return the blob as response

        with open(file_path,'rb') as excel_file:            
# Create BytesIO object
            excel_bytes = BytesIO(excel_file.read())        
# Create response
        response = HttpResponse(excel_bytes, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] ='attachment; filename="registerTemplate.xlsx"'
        return response
        
        
        

        

        
