from django.db import models
from django.utils.timezone import now

# Create your models here.


class Employee(models.Model):

    class Meta:
        db_table = "employee"

    # "employee" table columns
    name = models.CharField(max_length=35)
    address = models.CharField("email", max_length=35)
    age = models.IntegerField(default=18)
    join_date = models.DateTimeField(
        "employement_date", default=now, editable=True)


class Company(models.Model):

    class Meta:
        db_table = "company"

    # "company" table columns
    # with ForeignKey field always on the Many Table.
    employee_id = models.ForeignKey("Employee", on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    address = models.CharField("location", max_length=54)


class Salary(models.Model):

    class Meta:
        db_table = "salary"

    # "salary" table columns
    employee_id = models.ForeignKey("Employee", on_delete=models.CASCADE)
    currency = models.CharField(max_length=5)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
