# Generated by Django 4.1.2 on 2023-01-18 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City_Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stud_Name', models.CharField(max_length=30)),
                ('Stud_Age', models.IntegerField()),
                ('Stud_Phno', models.BigIntegerField()),
                ('Stud_City', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentApp.city')),
                ('Stud_Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentApp.course')),
            ],
        ),
    ]
