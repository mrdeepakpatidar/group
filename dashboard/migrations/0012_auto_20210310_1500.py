# Generated by Django 3.1.5 on 2021-03-10 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20210310_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='aadhar_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='intern',
            name='aadhar_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='aadhar_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trainee',
            name='aadhar_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
