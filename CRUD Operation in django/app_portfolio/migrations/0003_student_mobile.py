# Generated by Django 4.2.1 on 2023-07-08 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_portfolio', '0002_student_rollno'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mobile',
            field=models.CharField(default=0, max_length=10, verbose_name='Student Phone no.'),
        ),
    ]
