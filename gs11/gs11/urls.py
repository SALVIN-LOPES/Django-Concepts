from api import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.Student_api),
    path('studentapi/<str:pk>', views.Student_api),
]
