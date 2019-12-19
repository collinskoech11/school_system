# Generated by Django 3.0.1 on 2019-12-18 16:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20191218_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.UUIDField(default=uuid.UUID('402896b7-abdf-4f71-bfe5-9d98d9f07093'), help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
    ]