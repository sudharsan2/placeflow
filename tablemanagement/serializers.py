from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import users,userRoles,studentData, companyData, addUserExcel
from rest_framework.exceptions import AuthenticationFailed

class userRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = userRoles
        fields = "__all__"

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ['username','email','roles']

class addUserExcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = addUserExcel
        fields = ('excelFile')

class userRegistrationSerializer(serializers.ModelSerializer):
    
    roles = serializers.CharField(max_length =20)
    # password=serializers.CharField(max_length=255,min_length=5,write_only=True )
   

    class Meta:
        model = users
        fields = ['username', 'email', 'password', 'roles']

    def create(self, validated_data):
        roles_data = validated_data.pop('roles','student')
        role_instance, created = userRoles.objects.get_or_create(role = roles_data)
        validated_data['roles'] = role_instance
        # password = validated_data.get('password','welcome')
        validated_data['password'] = "welcome"
        user_instance= users.objects.create_user(**validated_data)
    
        return user_instance
        
        
# class loginSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=50, min_length=8, write_only=True)
#     username = serializers.CharField(max_length=255)

#     class Meta:
#         model = user
#         fields = ['username', 'password', 'tokens']
    
#     def validate(self, data):
#         username = data.get('username', '')
#         password = data.get('password', '')
#         user = authenticate(username=username, password=password)

#         if not user:
#             raise AuthenticationFailed('Invalid credentials')

#         return {
#             'username': user.username,
#             'tokens': user.tokens()
#         }

class loginSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=255,min_length=5,write_only=True )
    username=serializers.CharField(max_length=255)
            
    class Meta:
        model=users
        fields=['username','password','token','id']        
        
    def validate(self, obj):
        name=obj.get('username', '')
        password=obj.get('password', '')
        
        user = authenticate( username=name, password=password)
        
        if not user:
            raise AuthenticationFailed('Invalid Credentials')
            
        if not user.is_active:
            raise AuthenticationFailed('Account not valid, Contact admin')
        
        
        
        return {
            'username': user.username,
            'id': user.id,
            'token': user.token(),
            'example':'example'
        }




            
        