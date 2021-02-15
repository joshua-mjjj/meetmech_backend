from .models import *
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics
from .serializers import *
from rest_framework.decorators import api_view
from knox.models import AuthToken
from rest_framework import status
import numpy as np

class StatusViewSet(viewsets.ModelViewSet):
	permission_classes = [permissions.IsAuthenticated, ]
	# queryset = Status.objects.all()
	serializer_class = StatusSerializer
	def get_queryset(self):
		return  self.request.user.statuses.all() # using the related name "statuses" to query status of a user
	def perform_create(self, serializer):
		query = self.request.user.statuses.all()
		if(len(query) == 0):
			serializer.save(user=self.request.user)
		else:
			raise serializers.ValidationError(
                    {'status': 'A status already exists'}
                )
		
	def perform_update(self, serializer):
		serializer.save(user=self.request.user)

class ProfileViewSet(viewsets.ModelViewSet):
	permission_classes = [permissions.IsAuthenticated, ]
	# def get_permissions(self):
	# 	if self.action == "retrieve":
	# 		self.permission_classes = [permissions.AllowAny]
	# 	else:
	# 		self.permission_classes = [permissions.IsAuthenticated]

	# 	return super(ProfileViewSet, self).get_permissions()

	# queryset = Status.objects.all()
	serializer_class = ProfileSerializer
	def get_queryset(self):
		statuses = self.request.user.profiles.all()
		return  self.request.user.profiles.all() # using the related name "statuses" to query status of a user
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
		#saving a lead to its owner
		
	def perform_update(self, serializer):
		serializer.save(owner=self.request.user)

class ProfileViewSet_(viewsets.ModelViewSet):
	def get_permissions(self):
		if self.action == "retrieve":
			self.permission_classes = [permissions.AllowAny]
		else:
			self.permission_classes = [permissions.IsAuthenticated]

		return super(ProfileViewSet_, self).get_permissions()

	serializer_class = ProfileSerializer
	queryset = serviceProvider.objects.all()
	http_method_names = ['get']


# Register API
class RegisterAPI(generics.GenericAPIView):
	serializer_class = RegisterSerialzer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		return Response({
      		"user": UserSerializer(user, context=self.get_serializer_context()).data,
      		"token": AuthToken.objects.create(user)[1]
    		})

# Login API
class LoginAPI(generics.GenericAPIView):
	serializer_class = LoginSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data
		return Response({
      		"user": UserSerializer(user, context=self.get_serializer_context()).data,
      		"token": AuthToken.objects.create(user)[1]
    		})

# Get User API
class UserAPI(generics.RetrieveAPIView):
	permission_classes = [permissions.IsAuthenticated, ]
	serializer_class = UserSerializer

	# def get_object(self):
	# 	return self.request.user
	def get(self, request):
		user = request.user
		queryset = Status.objects.filter(user=user)
		serializer = UserSerializer(user, many=False)
		get_status = StatusSerializer(queryset, many=True)
		print(get_status)
		return Response({
      		"user": serializer.data,
      		"status": get_status.data
    		})

class AutoComplete(generics.RetrieveAPIView):
	permission_classes = [permissions.AllowAny, ]
	serializer_class = UserSerializer
	http_method_names = ['get']

	def get(self, request):
		serializer = UserSerializer(request.user, many=False)
		suggestions = ["Car wiring", "Wheel Alignment", "Electric Cars", "Engine Checking", "Wheel Balancing", "Flat Tyres", "Computer Aided Mechanics"]
		return Response({
      		"suggestions": suggestions
    		})

class NoteViewSet(viewsets.ModelViewSet):
	queryset = Note.objects.all()
	serializer_class = Note_Serializer