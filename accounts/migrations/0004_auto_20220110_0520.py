# Generated by Django 3.2.9 on 2022-01-10 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211222_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='county',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='vet',
            name='county',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
