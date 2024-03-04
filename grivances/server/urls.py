from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('api/student/', views.StudentModelList.as_view()),
    path('api/student/<str:pk>/', views.StudentModelDetail.as_view()),
    path('api/faculty/', views.FacultyModelList.as_view()),
    path('api/faculty/<str:pk>/', views.FacultyModelDetail.as_view()),
    path('api/complaint/', views.ComplaintModelList.as_view()),
    path('api/complaint/<int:pk>/', views.ComplaintModelDetail.as_view()),
    path('verify/<phone>/', views.getPhoneNumberRegistered.as_view()),
    path('api/user/<str:pk>/', views.UsersModelDetail.as_view()),
    path('api/user/', views.UsersModelList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
