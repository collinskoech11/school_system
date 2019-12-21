# Generated by Django 3.0.1 on 2019-12-20 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20191218_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='female_guardian',
        ),
        migrations.RemoveField(
            model_name='student',
            name='male_guardian',
        ),
        migrations.RemoveField(
            model_name='student',
            name='sponsor',
        ),
        migrations.AddField(
            model_name='student',
            name='father_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='father_first_name',
            field=models.CharField(help_text="Enter the first name of the student's male guardian", max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='father_phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='father_premium',
            field=models.BooleanField(blank=True, default=False, help_text='Do not edit this'),
        ),
        migrations.AddField(
            model_name='student',
            name='father_sir_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='mother_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='mother_first_name',
            field=models.CharField(help_text="Enter the first name of the student's female guardian", max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='mother_phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='mother_premium',
            field=models.BooleanField(blank=True, default=False, help_text='Do not edit this'),
        ),
        migrations.AddField(
            model_name='student',
            name='mother_sir_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='sponsor_company_name',
            field=models.CharField(blank=True, help_text='Only if the Sponsor is a company', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='sponsor_first_name',
            field=models.CharField(blank=True, help_text='First name of sponsor if applicable', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='sponsor_premium',
            field=models.BooleanField(blank=True, default=False, help_text='Do not edit this'),
        ),
        migrations.AddField(
            model_name='student',
            name='sponsor_sir_name',
            field=models.CharField(blank=True, help_text='Sir name of sponsor if applicable', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='father_alive',
            field=models.BooleanField(default=True, help_text='Is the father alive?', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mother_alive',
            field=models.BooleanField(default=True, help_text='Is the mother alive?', null=True),
        ),
        migrations.DeleteModel(
            name='Father',
        ),
        migrations.DeleteModel(
            name='Mother',
        ),
        migrations.DeleteModel(
            name='Sponsor',
        ),
    ]
