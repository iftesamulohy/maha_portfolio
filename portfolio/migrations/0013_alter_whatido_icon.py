# Generated by Django 4.0.5 on 2022-09-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_whatido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatido',
            name='icon',
            field=models.CharField(max_length=35),
        ),
    ]
