# Generated by Django 4.0.6 on 2022-12-26 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aiproject', '0012_postimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='Duty',
            field=models.CharField(default='共授教師', max_length=50),
        ),
    ]
