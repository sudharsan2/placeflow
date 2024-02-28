from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import userRoles,users
from . serializers import userRegistrationSerializer,loginSerializer,addUserExcelSerializer,userRoleSerializer,userSerializer
from rest_framework import status
import pandas as pd


class userRegistrationAPI(APIView):
    def post(self, request):
        payload = request.data
        serializer = userRegistrationSerializer(data=payload)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
"-----------------------------------------------------------------------------------------------------------------------------"
# class userRegistrationWithExcelAPI(APIView):
#     def post(self,request):
#         payload = request.data
#         serializer = addUserExcelSerializer(data=payload)
#         if serializer.is_valid():
#             instance = serializer.save()
#             file_path = instance.excelFile.path
#             data = self.readExcel(file_path)
    
#     def readExcel(file_path):
#         df = pd.read_excel('excel_testing/Book9.xlsx', header=None)

#         # Extract column names from row 3
#         columns = df.iloc[2].tolist()

#         # Extract data starting from row 4
#         data = df.iloc[3:]

#         # Reset index to make it easier to work with
#         data = data.reset_index(drop=True)

#         # Create a list of dictionaries using column names and corresponding row values
#         result_list = [dict(zip(columns, row)) for index, row in data.iterrows()]

#         return result_list
"-----------------------------------------------------------------------------------------------------------------------------"
class loginAPI(APIView):
    def post(self,request):
        payload = request.data
        serializer = loginSerializer(data=payload)

        serializer.is_valid(raise_exception=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

# class loginAPI(APIView):
#     def post(self, request):
#         payload = request.data
#         serializer = loginSerializer(data=payload)
#         serializer.is_valid(raise_exception=True)

#         # The user is already authenticated in the serializer
#         tokens = serializer.validated_data['tokens']

#         return Response(tokens, status=status.HTTP_200_OK)


        
"-----------------------------------------------------------------------------------------------------------------------------"
class inserUserRoles(APIView):
    def post(self, request):
        payload = request.data
        serializer = userRoleSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)

class getUserRoles(APIView):
    def get(self,request,*args,**kwargs):
        data1 = userRoles.objects.all()
        serializer = userRoleSerializer(data1, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class getusers(APIView):
    def get(self,request):
        data1 = users.objects.all()
        serializer = userSerializer(data1,many= True)
        return Response(serializer.data , status=status.HTTP_200_OK)