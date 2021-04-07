from django.urls import path
from . import views
app_name="EMS"
urlpatterns=[
    path(r'employee/',views.home,name="employee"),
    path(r'employee/attendance/',views.Attendance,name="attendance"),
]
