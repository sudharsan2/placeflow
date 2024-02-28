from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import postcompanyDataSerializer,getcompanyDataSerializer,excelRegistrationSerializer
from tablemanagement.models import companyData
from rest_framework.response import Response
from rest_framework import status
import base64
from django.http import HttpRequest
import pandas as pd
import requests
from io import BytesIO

# Create your views here.

class enterCompanyDataAPI(APIView):
    def post(self, request):
        payload = request.data
        serializer = postcompanyDataSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
        return Response({"message": "succesfully created"}, status=status.HTTP_201_CREATED)
    
# class excelTesting(APIView):
#     def post(self, request):
#         payload = request.data
#         excel_binary_data = payload['ex']

class getallCompanyDataAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            payload = companyData.objects.all()
            serializer = getcompanyDataSerializer(payload, many= True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

        
class handleExcelFileAPI(APIView):
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
                            "password": data_dict["password"], 
                            "email": data_dict["email"],
                            "roles": data_dict["roles"]}  
            serializer = excelRegistrationSerializer(data=request_data)
            if serializer.is_valid():
                serializer.save()
                responses.append(serializer.data)
        return Response(responses, status=status.HTTP_201_CREATED)
            


    

        

        
