# Generated by Django 5.0.2 on 2024-04-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0002_remove_resume_education_resume_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='education',
            field=models.SmallIntegerField(default=0, verbose_name='Educational qualifications (recent N, 0 for none)'),
        ),
    ]
