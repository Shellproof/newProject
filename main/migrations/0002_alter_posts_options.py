# Generated by Django 5.0.6 on 2024-06-26 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-created_date'], 'verbose_name': 'Записи', 'verbose_name_plural': 'Записи'},
        ),
    ]