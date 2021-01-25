from django.urls import path, include
from knox import views as knox_views
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from .api import *
from .views import *

router = DefaultRouter()
router.register(r'user_status', StatusViewSet, basename='status')
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'profiles_get', ProfileViewSet_, basename='list_profiles')
router.register(r'notes', NoteViewSet, basename='notes')

schema_view = get_swagger_view(title='MeetMech API')

urlpatterns = [
	path('auth', include('knox.urls')),
    path('auth/register', RegisterAPI.as_view()),
    path('auth/login', LoginAPI.as_view()),
    path('auth/user', UserAPI.as_view()),
    path('auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
	path('user_request/', UsersCreate, name="users"),
	path('user_list/', UsersList, name="users_list"),
	path('autocomplete/', AutoComplete.as_view(), name="auto_completes"),
	path('', include(router.urls)),

]