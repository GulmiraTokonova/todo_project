# Generated by Django 4.0.3 on 2022-06-25 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tomeet',
            name='date_of_meeting',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
