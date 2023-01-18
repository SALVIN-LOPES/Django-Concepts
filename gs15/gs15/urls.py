from api import views
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentList/',views.StudentList.as_view(),name="student"),
    path('studentCreate/',views.StudentCreate.as_view(),name="studentCreate"),
    path('studentRetrieve/<str:pk>/',views.StudentRetrieve.as_view(),name="studentRetrieve"),
    path('studentUpdate/<str:pk>/',views.StudentUpdate.as_view(),name="studentUpdate"),
    path('studentDelete/<str:pk>/',views.StudentDelete.as_view(),name="studentDelete"),
    
    # path('studentapi/', views.StudentList.as_view()), # delete request
    # path('studentapi/', views.StudentCreate.as_view()), # delete request
    # path('studentapi/<str:pk>/', views.StudentRetrieve.as_view()), # delete request
    # path('studentapi/<str:pk>/', views.StudentUpdate.as_view()), # delete request
    # path('studentapi/<str:pk>/', views.StudentDelete.as_view()), # delete request
    # path('studentapi/<str:pk>/', views.RUDStudentRetrieve.as_view()), # delete request
]
