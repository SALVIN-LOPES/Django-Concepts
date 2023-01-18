
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/<str:pk>', views.student_detail),
    path('student/', views.student_list),
]
