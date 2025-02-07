from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_student, name='create_student'),
    path('', views.student_list, name='student_list'),
    path('<int:pk>/', views.student_detail, name='student_detail'),
    path('<int:pk>/edit/', views.update_student, name='update_student'),
    path('<int:pk>/delete/', views.delete_student, name='delete_student'),
]
