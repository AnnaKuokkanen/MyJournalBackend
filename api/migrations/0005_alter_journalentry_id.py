# Generated by Django 4.1.3 on 2022-11-14 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_delete_user_journalentry_content_journalentry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
