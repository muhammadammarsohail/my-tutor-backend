from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # a post api
    path('regapplicant/', views.ApplicantView.as_view(), name='applicants'),
    path('applicant/<int:pk>/', views.ApplicantView.as_view(), name='showApplicants'),
    path('all-applicants/', views.AllApplicantView.as_view(), name='showApplicants'),
    path('hire-applicant/<int:pk>/',views.hire)

    # path('regapplicants/', views.ApplicantView.as_view(), name='applicants'),

]