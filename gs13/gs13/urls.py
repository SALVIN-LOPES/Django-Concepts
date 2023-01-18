from api import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/', views.StudentList.as_view()), # get list request
    # path('studentapi/', views.StudentCreate.as_view()), # post request
    # path('studentapi/<str:pk>/', views.StudentRetrieve.as_view()), # get request
    # path('studentapi/<str:pk>/', views.StudentUpdate.as_view()), # update request
    # path('studentapi/<str:pk>/', views.StudentUpdatePartial.as_view()), # partial update request
    path('studentapi/<str:pk>/', views.StudentDelete.as_view()), # delete request
]
