# Generated by Django 5.1.2 on 2024-12-11 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0003_alter_kadai_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kadai',
            name='category',
            field=models.CharField(choices=[('基本区分', '基本'), ('応用区分', '応用'), ('チュートリアル', 'チュートリアル')], default='基本区分', max_length=10, verbose_name='問題区分'),
        ),
    ]
