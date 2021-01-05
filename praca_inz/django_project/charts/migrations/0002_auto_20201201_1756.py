# Generated by Django 3.1.3 on 2020-12-01 17:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinputdate',
            old_name='date',
            new_name='date_from',
        ),
        migrations.AddField(
            model_name='userinputdate',
            name='date_to',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
