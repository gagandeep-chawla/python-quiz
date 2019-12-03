from django.urls import path
from student_detials.views import StudentRegistration

urlpatterns = [
    path('registration/', StudentRegistration.as_view(),name = 'registration'),
]