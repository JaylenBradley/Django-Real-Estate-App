# Generated by Django 4.2.16 on 2024-10-18 02:24

from django.db import migrations, models
#The migrations folder keeps record of changes made to the DB, this file is a record of the change
#Run "python3 manage.py makemigrations" to create a new record of the changes made to the DB
#Run "python3 manage.py migrate" to apply the changes to the DB

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('num_bedrooms', models.IntegerField()),
                ('num_bathrooms', models.IntegerField()),
                ('square_footage', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
