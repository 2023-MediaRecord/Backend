# Generated by Django 4.0.3 on 2023-09-06 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_record_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='liked',
            field=models.BooleanField(default=0),
        ),
    ]