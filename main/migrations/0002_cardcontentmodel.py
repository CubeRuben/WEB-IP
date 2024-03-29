# Generated by Django 4.1.3 on 2023-04-16 07:20

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardContentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.TextField()),
                ('card_description', models.TextField()),
                ('blender_mesh', models.FileField(upload_to=main.models.CardContentModel.mesh_content_path)),
                ('fbx_mesh', models.FileField(upload_to=main.models.CardContentModel.mesh_content_path)),
                ('preview_mesh', models.FileField(upload_to=main.models.CardContentModel.mesh_content_path)),
                ('textures', django.contrib.postgres.fields.ArrayField(base_field=models.FileField(upload_to=main.models.CardContentModel.texture_content_path), size=None)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='main.cardtagsmodel')),
            ],
        ),
    ]
