from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    manager_id = models.IntegerField()
    department_id = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
