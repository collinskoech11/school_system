# Generated by Django 3.0.1 on 2019-12-26 09:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0041_auto_20191226_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.CharField(default=uuid.UUID('4f0f4c44-05d5-4584-aa05-833f1c15c04e'), help_text='Unique ID for this particular book across whole library', max_length=20, primary_key=True, serialize=False),
        ),
    ]
