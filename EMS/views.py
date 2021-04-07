from django.shortcuts import render
from .forms import AttendanceForm
# Create your views here.
def home(request):
    return render(request,'home.html')
def testFile(request):
    return render(request,'test.html',)
def Attendance(request):
    if(request.method=="POST"):
        attaind=AttendanceForm(request.POST)
        if(attaind.is_valid()):
            return render(request,'attendance.html')
    else:
        attaind=AttendanceForm()
    return render(request,'attendance.html',context={'attaind':attaind})
