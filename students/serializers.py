from rest_framework import serializers
from CIR.serializers import genderSerializer,departmentSerializer,arrearSerializer
from tablemanagement.models import studentData

class getstudentDataSerializer(serializers.ModelSerializer):
    gender = genderSerializer()
    department = departmentSerializer()
    standing_Arrears = arrearSerializer()
    arrear_history = arrearSerializer()

    class Meta:
        model = studentData
        fields = "__all__"

