# Generated by Django 5.1.3 on 2024-11-10 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empApp', '0002_alter_employee_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Programmers', models.ManyToManyField(to='empApp.programmer')),
            ],
        ),
    ]
