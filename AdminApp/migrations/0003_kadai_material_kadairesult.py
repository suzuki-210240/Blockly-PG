# Generated by Django 5.1.3 on 2024-12-06 13:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0002_fileupload'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kadai',
            fields=[
                ('kadai_id', models.AutoField(primary_key=True, serialize=False)),
                ('kadai_name', models.CharField(max_length=40, unique=True)),
                ('python_file_name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'kadai_table',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(max_length=40, unique=True)),
                ('html_file_name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'materials_table',
            },
        ),
        migrations.CreateModel(
            name='KadaiResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achieve', models.CharField(max_length=1)),
                ('kadai_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.kadai')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'kadai_achieve_table',
            },
        ),
    ]
