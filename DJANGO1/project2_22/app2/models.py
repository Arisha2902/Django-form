from django.db import models

class Emp(models.Model):
    emp_name=models.CharField(max_length=30)
    emp_id=models.IntegerField()
    emp_contact=models.IntegerField()
    def __str__(self):
        return self.emp_name+" "+str(self.emp_id)+" "+str(self.emp_contact)