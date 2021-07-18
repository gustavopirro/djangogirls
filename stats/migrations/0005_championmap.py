# Generated by Django 3.2.5 on 2021-07-18 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0004_auto_20210717_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChampionMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_name', models.CharField(max_length=100)),
                ('winrate', models.IntegerField(default=0)),
                ('match_count', models.IntegerField(default=0)),
                ('confidence_interval_plus', models.IntegerField(default=0)),
                ('champion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.champion')),
            ],
        ),
    ]
