# Generated by Django 3.0.1 on 2019-12-18 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20191218_1539'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disciplinaryissue',
            options={'ordering': ['date', 'student']},
        ),
        migrations.AlterModelOptions(
            name='healthissue',
            options={'ordering': ['date', 'student']},
        ),
    ]
