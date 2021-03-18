# Generated by Django 3.1.5 on 2021-03-10 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20210310_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='aadhar_no',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='contact_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='father_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='pin_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='intern',
            name='aadhar_no',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='intern',
            name='father_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='intern',
            name='pin_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='calling',
            field=models.CharField(default=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='lead',
            name='whatsapp',
            field=models.CharField(default=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='staff',
            name='aadhar_no',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='trainee',
            name='aadhar_no',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='trainee',
            name='pin_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='aadhar_no',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='contact_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='father_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='pin_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
