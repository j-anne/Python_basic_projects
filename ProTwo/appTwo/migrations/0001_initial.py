# Generated by Django 3.2.8 on 2021-10-30 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128, unique=True)),
                ('last_name', models.CharField(max_length=128, unique=True)),
                ('email', models.CharField(max_length=128, unique=True)),
            ],
        ),
    ]
