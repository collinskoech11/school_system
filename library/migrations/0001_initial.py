# Generated by Django 3.0.1 on 2019-12-18 10:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academics', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('085116bf-4a0a-49eb-a0c6-c113d09cfaea'), help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(blank=True, help_text='Enter a brief description of the Book', max_length=1000, null=True)),
                ('ISBN', models.CharField(blank=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, null=True, verbose_name='ISBN')),
                ('author', models.ManyToManyField(to='library.Author')),
                ('subject', models.ManyToManyField(help_text='Select Subject', to='academics.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='BookType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Eg: story book, dictionary, course text book', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BorrowBookInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('l', 'On loan'), ('a', 'Available')], default='l', help_text='Book Availability', max_length=1)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.Book')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
            ],
            options={
                'ordering': ['date_due_back'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='type',
            field=models.ManyToManyField(help_text='Select a book type', to='library.BookType'),
        ),
    ]
