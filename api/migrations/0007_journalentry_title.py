# Generated by Django 4.1.3 on 2022-11-25 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_journalentry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalentry',
            name='title',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
