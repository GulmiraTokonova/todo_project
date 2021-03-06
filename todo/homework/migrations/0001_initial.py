# Generated by Django 4.0.3 on 2022-06-16 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToMeet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persone', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField(verbose_name=10)),
                ('date_of_meeting', models.DateField(auto_now_add=True)),
                ('comment', models.CharField(max_length=200)),
                ('is_closed', models.BooleanField(default=False)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
    ]
