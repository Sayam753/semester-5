from django.db import models

# Create your models here.


class Student(models.Model):
    """Student in a university model."""

    roll_number = models.CharField(max_length=12, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    program = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=20)
    cgpa = models.FloatField()
    year_of_graduation = models.IntegerField()

    def __str__(self):
        """Representation of Student model."""
        return f"{self.roll_number}: {self.first_name} {self.last_name}, {self.email}, {self.cgpa}\
        {self.year_of_graduation}"
