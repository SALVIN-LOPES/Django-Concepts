from api import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('studentapi/', views.LCStudentAPI.as_view()), # delete request
    path('studentapi/<str:pk>/', views.RUDStudentRetrieve.as_view()), # delete request
]
