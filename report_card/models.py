from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    department = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.department

    class Meta:
        ordering = ["department"]


class Subject(models.Model):
    subject_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.subject_name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(
        Department, related_name="students", on_delete=models.CASCADE, null=True
    )
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    username = models.CharField(max_length=30, default="")
    roll_number = models.CharField(max_length=20, default="")
    email = models.EmailField(default="")
    password = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ["first_name"]


class SubjectMarks(models.Model):
    student = models.ForeignKey(
        Student, related_name="studentmarks", on_delete=models.CASCADE
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    rank = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.student.first_name} - {self.subject.subject_name} - {self.marks}"

    class Meta:
        unique_together = ["student", "subject"]


class ReportCard(models.Model):
    student = models.ForeignKey(
        Student, related_name="studentreport", on_delete=models.CASCADE
    )
    student_rank = models.IntegerField()
    date_of_generation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["student_rank", "date_of_generation"]


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    username = models.CharField(max_length=30, default="")
    email = models.EmailField(default="")
    password = models.CharField(max_length=100, default="default_password")
