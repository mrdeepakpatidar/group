# Generated by Django 3.1.5 on 2021-03-10 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20210310_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='calling',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
