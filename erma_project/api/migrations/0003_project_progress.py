# Generated by Django 3.0.3 on 2020-02-27 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200227_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='progress',
            field=models.IntegerField(choices=[(0, 'NOT STARTED'), (1, 'IS WORKING'), (3, 'DONE')], default=0),
        ),
    ]
