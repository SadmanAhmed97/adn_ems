# Generated by Django 3.1.2 on 2020-11-05 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='adn_id',
            field=models.IntegerField(),
        ),
    ]