# Generated by Django 5.0.1 on 2024-02-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registermodel',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
