# Generated by Django 5.0 on 2023-12-15 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_duel_options_live'),
    ]

    operations = [
        migrations.AddField(
            model_name='duel',
            name='live',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Live',
        ),
    ]
