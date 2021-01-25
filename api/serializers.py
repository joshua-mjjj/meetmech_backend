from rest_framework import serializers
from .models import * 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# users Serializer
class User_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     services = serializers.SerializerMethodField()

#     def get_services(self, obj):
#         services = UserService.objects.filter(user=obj)
#         return UserServiceSerializer(services, many=True).data

# serviceProvider Serializer
class ProfileSerializer(serializers.ModelSerializer):
	status = serializers.SerializerMethodField()

	class Meta:
		model = serviceProvider 
		fields = '__all__'

	def get_status(self, obj):
		status_data = Status.objects.filter(owner_username=obj)
		data = StatusSerializer(status_data, many=True).data
		return data

# serviceProvider Serializer
class StatusSerializer(serializers.ModelSerializer):
  class Meta:
    model = Status 
    fields = '__all__'

#User Serializer
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email')

#Register Serializer
class RegisterSerialzer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'password')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		user = User.objects.create_user(
			validated_data['username'],
			validated_data['email'],
			validated_data['password'])

		return user

#Login Serializer
class LoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()

	def validate(self, data):
		user = authenticate(**data)
		if user and user.is_active:
			return user
		raise serializers.ValidationError('Incorrect Credentials')

class Note_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Note
		fields = '__all__'




