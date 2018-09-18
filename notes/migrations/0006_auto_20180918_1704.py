# Generated by Django 2.1.1 on 2018-09-18 17:04

from django.db import migrations, models
import notes.models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_note_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='expiration',
            field=models.DateTimeField(default=notes.models.get_exp),
        ),
    ]