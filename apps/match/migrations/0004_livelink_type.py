# Generated by Django 3.0.10 on 2022-02-28 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0003_livelink_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='livelink',
            name='type',
            field=models.IntegerField(choices=[(0, 'Youtube')], default=0, verbose_name='Type'),
        ),
    ]
