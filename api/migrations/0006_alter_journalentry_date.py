# Generated by Django 4.1.3 on 2022-11-14 19:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_journalentry_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]