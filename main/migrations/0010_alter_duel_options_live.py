# Generated by Django 5.0 on 2023-12-15 16:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_duel_player1_alter_duel_player2_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='duel',
            options={'ordering': ['table']},
        ),
        migrations.CreateModel(
            name='Live',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duel', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.duel')),
            ],
        ),
    ]
