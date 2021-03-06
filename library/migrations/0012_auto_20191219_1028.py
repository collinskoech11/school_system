# Generated by Django 3.0.1 on 2019-12-19 10:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_auto_20191219_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.CharField(default=uuid.UUID('156821c7-dc2e-4983-9dc1-9c92cef5ce73'), help_text='Unique ID for this particular book across whole library', max_length=20, primary_key=True, serialize=False),
        ),
    ]
