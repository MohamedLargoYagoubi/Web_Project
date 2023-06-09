# Generated by Django 4.1.7 on 2023-03-24 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="jugador",
            name="años_exp",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="jugador",
            name="edad",
            field=models.IntegerField(default=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="jugador",
            name="posicion",
            field=models.CharField(default="Delantero", max_length=256),
            preserve_default=False,
        ),
    ]
