# Generated by Django 3.1.5 on 2021-03-13 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_auto_20210313_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainee',
            name='traineecource',
        ),
        migrations.AddField(
            model_name='internattendance',
            name='half_day',
            field=models.CharField(default='No', max_length=100),
        ),
        migrations.AddField(
            model_name='trainee',
            name='trainee_cource',
            field=models.CharField(blank=True, default=True, max_length=100, null=True),
        ),
    ]
