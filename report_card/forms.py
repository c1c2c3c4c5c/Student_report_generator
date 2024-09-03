from django import forms
from django.contrib.auth.hashers import make_password
from .models import *


class MarkForm(forms.Form):
    roll_number = forms.CharField(max_length=20, label="Roll Number")
    input_method = forms.BooleanField(required=False)
    file = forms.FileField(required=False)
    subject1 = forms.ModelChoiceField(queryset=Subject.objects.all(), label="Subject 1")
    marks1 = forms.DecimalField(max_digits=5, decimal_places=2, label="Marks 1")
    subject2 = forms.ModelChoiceField(queryset=Subject.objects.all(), label="Subject 2")
    marks2 = forms.DecimalField(max_digits=5, decimal_places=2, label="Marks 2")
    subject3 = forms.ModelChoiceField(queryset=Subject.objects.all(), label="Subject 3")
    marks3 = forms.DecimalField(max_digits=5, decimal_places=2, label="Marks 3")
    subject4 = forms.ModelChoiceField(queryset=Subject.objects.all(), label="Subject 4")
    marks4 = forms.DecimalField(max_digits=5, decimal_places=2, label="Marks 4")
    subject5 = forms.ModelChoiceField(queryset=Subject.objects.all(), label="Subject 5")
    marks5 = forms.DecimalField(max_digits=5, decimal_places=2, label="Marks 5")

    def save(self, *args, **kwargs):
        student = Student.objects.get(roll_number=self.cleaned_data["roll_number"])
        for i in range(1, 6):
            SubjectMarks.objects.create(
                student=student,
                subject=self.cleaned_data[f"subject{i}"],
                marks=self.cleaned_data[f"marks{i}"],
            )


class TeacherRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Teacher
        fields = ["first_name", "last_name", "username", "email", "password"]

    def save(self, commit=True):
        teacher = super().save(commit=False)
        teacher.password = make_password(self.cleaned_data["password"])
        if commit:
            teacher.save()
        return teacher


class StudentRegistrationForm(forms.ModelForm):
    roll_number = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Student
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "roll_number",
            "password",
        ]

    def save(self, commit=True):
        student = super().save(commit=False)
        student.password = make_password(self.cleaned_data["password"])
        if commit:
            student.save()
        return student


class UploadFileForm(forms.Form):
    file = forms.FileField()
