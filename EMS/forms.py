from django import forms
from django.core import validators
# for Attendance
class AttendanceForm(forms.Form):
    Email=forms.CharField(widget=forms.TextInput(attrs={
                                                    'class':'form-control',
                                                    'placeholder':'Email',
                                                    }))
    Attdendance_date=forms.DateTimeField(widget=forms.DateTimeInput(attrs={
                                                                    'class':'form-control',
                                                                    'placeholder':'Attdendance Date',
                                                                    }))
    status=forms.CharField(widget=forms.TextInput(attrs={
                                                        'class':'form-control',
                                                        'placeholder':'status',
                                                        }))
    Day_type=forms.CharField(widget=forms.TextInput(attrs={
                                                        'class':'form-control',
                                                        'placeholder':'Day Type',
                                                        }))
    Branch=forms.CharField(widget=forms.TextInput(attrs={
                                                        'class':'form-control',
                                                        'placeholder':'Branch',
                                                        }))
    Fitting_center=forms.CharField(widget=forms.TextInput(attrs={
                                                        'class':'form-control',
                                                        'placeholder':'Fitting Center',
                                                        }))
    remarks=forms.Textarea()

class AttendanceHistory(forms.Form):
    from_date=forms.DateField()
    to_date=forms.DateField()
    employee_code=forms.CharField()             #foreign key of employee id

class LeaveRequest(forms.Form):
    # forms.RadioSelect(choices=('self','Reportee'))
    CHOICES=[('1','self'),('1','Reportee')]
    Lrequest_type=forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES)
    employee_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    LeaveType=forms.CharField(max_length=100)
    Leave_From_date=forms.DateField()
    leave_to_date=forms.DateField()
    to_be_approved_by=forms.CharField(max_length=100)
    reason=forms.CharField(max_length=100)
    type=forms.CharField(max_length=100)
    Leave_remarks=forms.Textarea()
    attachment=forms.FileField(allow_empty_file=True)
