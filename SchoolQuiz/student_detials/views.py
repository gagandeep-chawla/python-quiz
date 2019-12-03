from django.shortcuts import render
from django.views import View
from django.shortcuts import render


from student_detials.models import Student_Info

# Create your views here.

class StudentRegistration(View):
    
    def get(self,request):
        return render(request,'Student_detials/registration.html',{})
    
    