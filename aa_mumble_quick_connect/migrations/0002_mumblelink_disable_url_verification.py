# Generated by Django 4.2.19 on 2025-02-14 07:35

# Django
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aa_mumble_quick_connect", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="mumblelink",
            name="disable_url_verification",
            field=models.BooleanField(
                default=False,
                help_text="If checked, the Mumble channel URL will not be verified against what is configured for this Auth instance when saving the link. Only use this if you are sure the URL is correct and the Mumble server is controlled by this Auth instance.",
                verbose_name="Disable Mumble channel URL verification",
            ),
        ),
        migrations.AlterField(
            model_name="mumblelink",
            name="url",
            field=models.CharField(help_text="URL to the channel", max_length=255),
        ),
    ]
