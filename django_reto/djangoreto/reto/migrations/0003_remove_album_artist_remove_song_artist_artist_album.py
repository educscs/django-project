# Generated by Django 4.1.4 on 2022-12-20 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reto", "0002_alter_album_id_alter_artist_id_alter_song_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="album",
            name="artist",
        ),
        migrations.RemoveField(
            model_name="song",
            name="artist",
        ),
        migrations.AddField(
            model_name="artist",
            name="album",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="reto.album"
            ),
        ),
    ]