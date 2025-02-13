# Generated by Django 4.2.19 on 2025-02-13 12:30

# Django
import django.db.models.deletion
from django.db import migrations, models

# AA Mumble Quick Connect
import aa_mumble_quick_connect.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="General",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "permissions": (("basic_access", "Can access this app"),),
                "managed": False,
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="Section",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the section", max_length=255, unique=True
                    ),
                ),
            ],
            options={
                "verbose_name": "Section",
                "verbose_name_plural": "Sections",
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="MumbleLink",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the Mumble channel", max_length=255
                    ),
                ),
                (
                    "url",
                    models.CharField(
                        help_text="URL to the channel",
                        max_length=255,
                        validators=[aa_mumble_quick_connect.models.validate_mumble_url],
                    ),
                ),
                (
                    "section",
                    models.ForeignKey(
                        blank=True,
                        help_text="Section the Mumble channel belongs to. (Optional)",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="mumble_links",
                        to="aa_mumble_quick_connect.section",
                        verbose_name="Section",
                    ),
                ),
            ],
            options={
                "verbose_name": "Mumble Link",
                "verbose_name_plural": "Mumble Links",
                "default_permissions": (),
            },
        ),
    ]
