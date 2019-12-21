# Generated by Django 3.0.1 on 2019-12-21 22:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0028_auto_20191221_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.CharField(default=uuid.UUID('11cb6f9a-8d23-4fab-8da0-40bde49b2ada'), help_text='Unique ID for this particular book across whole library', max_length=20, primary_key=True, serialize=False),
        ),
    ]