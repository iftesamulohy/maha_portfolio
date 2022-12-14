# Generated by Django 4.0.5 on 2022-09-05 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_responsibilities_workexperience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('profile_image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
    ]
