from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('regapplicants/', views.ApplicantView.as_view(), name='applicants'),
    path('hire-applicant/<int:pk>/',views.hire),
    path('training-classes/', views.TrainingClassesView.as_view(), name='training')
]