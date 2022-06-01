from django.urls import path
from AppCoder import views


urlpatterns = [
    path('curso/', views.curso, name="Curso"),
    path('profesores/', views.profesores),
]
