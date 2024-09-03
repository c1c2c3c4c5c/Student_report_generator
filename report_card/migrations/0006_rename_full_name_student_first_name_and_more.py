# Generated by Django 4.2.11 on 2024-04-17 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_card', '0005_remove_student_user_remove_teacher_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='full_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='full_name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
