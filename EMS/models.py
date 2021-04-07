from django.db import models
from django.utils import timezone
# Create your models here.
POST_CHOICES=(
    ('HR','HR'),
    ('Developer',"Developer"),
    ("Maneger","Maneger"),
)
class employee(models.Model):
    e_id=models.AutoField(primary_key=True)
    e_name=models.CharField(max_length=100)
    e_email=models.EmailField()
    e_post=models.CharField(max_length=100,choices=POST_CHOICES,default="")
    e_salary=models.BigIntegerField()
    e_bank_AC_no=models.CharField(max_length=500)
    e_bank_AC_Branch=models.CharField(max_length=100)
    e_bank_AC_IFSC_CODE=models.CharField(max_length=100)
    e_photo=models.ImageField(upload_to="images/Employee_profile")
    e_qualification=models.TextField()
    e_CV=models.FileField(upload_to='images/Employee_profile/CV')
    e_contact=models.CharField(max_length=10)
    e_joining_date=models.DateTimeField(auto_now_add=True)
    e_experience=models.CharField(max_length=22,default="Year:0 Months:0 Days:0 ")

    def __str__(self):
        return self.e_email
    def Experience_count(self):
        current=timezone.now()
        print(current)
        print(self.e_experience)
