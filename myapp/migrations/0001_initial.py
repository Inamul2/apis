# Generated by Django 4.0.4 on 2022-09-28 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerData',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('address', models.TextField()),
                ('phoneNumber', models.CharField(max_length=20)),
                ('emailAddress', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('pinCode', models.IntegerField()),
            ],
        ),
    ]
