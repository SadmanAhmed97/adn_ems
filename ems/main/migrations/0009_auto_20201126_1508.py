# Generated by Django 3.1.2 on 2020-11-26 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20201122_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='alternate_email',
            field=models.EmailField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='alternate_phone',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], default='null', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_employee',
            field=models.BooleanField(default=True),
        ),
    ]
