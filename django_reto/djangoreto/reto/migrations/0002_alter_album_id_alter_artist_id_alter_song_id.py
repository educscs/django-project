# Generated by Django 4.1.4 on 2022-12-20 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reto", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="id",
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="artist",
            name="id",
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="song",
            name="id",
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
