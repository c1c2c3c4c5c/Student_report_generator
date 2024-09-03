# Generated by Django 4.2.11 on 2024-04-17 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report_card', '0008_teacher_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100, null=True)),
            ],
            options={
                'ordering': ['department'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='grade',
            name='course',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='student',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='course',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='roll_number',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='student_name',
        ),
        migrations.AlterModelOptions(
            name='reportcard',
            options={'ordering': ['student_rank', 'date_of_generation']},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['first_name']},
        ),
        migrations.RenameField(
            model_name='reportcard',
            old_name='generated_on',
            new_name='date_of_generation',
        ),
        migrations.RenameField(
            model_name='reportcard',
            old_name='total_credits',
            new_name='student_rank',
        ),
        migrations.RemoveField(
            model_name='reportcard',
            name='academic_year',
        ),
        migrations.RemoveField(
            model_name='reportcard',
            name='gpa',
        ),
        migrations.RemoveField(
            model_name='reportcard',
            name='grades',
        ),
        migrations.RemoveField(
            model_name='reportcard',
            name='semester',
        ),
        migrations.AlterField(
            model_name='reportcard',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentreport', to='report_card.student'),
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
        migrations.DeleteModel(
            name='Mark',
        ),
        migrations.AddField(
            model_name='subjectmarks',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentmarks', to='report_card.student'),
        ),
        migrations.AddField(
            model_name='subjectmarks',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report_card.subject'),
        ),
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='report_card.department'),
        ),
        migrations.AlterUniqueTogether(
            name='subjectmarks',
            unique_together={('student', 'subject')},
        ),
    ]
