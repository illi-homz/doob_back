# Generated by Django 4.2 on 2023-05-03 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_event_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='message_id',
            field=models.SmallIntegerField(default=0, editable=False),
        ),
    ]
