# Generated by Django 4.1.3 on 2022-11-14 02:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_journal_entry_journalentry'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='journalentry',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='journalentry',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
