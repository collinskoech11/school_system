# Generated by Django 3.0.1 on 2019-12-26 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0022_auto_20191226_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='examperformance',
            name='grade',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('Z', 'Z'), ('Y', 'Y')], max_length=1, null=True),
        ),
    ]
