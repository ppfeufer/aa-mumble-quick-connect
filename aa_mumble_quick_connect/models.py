"""
App Models
"""

# Django
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


def validate_mumble_url(url: str):
    """
    Validate Mumble URL

    :param url:
    :type url:
    :return:
    :rtype:
    """

    mumble_base_url = f"mumble://{settings.MUMBLE_URL}"

    if not url.startswith(mumble_base_url):
        raise ValidationError(
            _(f"Your Mumble channel URL must start with '{mumble_base_url}'")
        )

    return url


class General(models.Model):
    """
    Meta model for app permissions
    """

    class Meta:
        """
        Meta definitions
        """

        managed = False
        default_permissions = ()
        permissions = (("basic_access", "Can access this app"),)


class Section(models.Model):
    """
    Section model
    """

    name = models.CharField(
        max_length=255, unique=True, help_text=_("Name of the section")
    )

    class Meta:  # pylint: disable=too-few-public-methods
        """
        Meta definitions
        """

        default_permissions = ()
        verbose_name = _("Section")
        verbose_name_plural = _("Sections")

    def __str__(self) -> str:
        return self.name


class MumbleLink(models.Model):
    """
    Mumble link model
    """

    section = models.ForeignKey(
        to=Section,
        on_delete=models.SET_NULL,
        related_name="mumble_links",
        verbose_name=_("Section"),
        null=True,
        blank=True,
    )
    name = models.CharField(
        max_length=255, help_text=_("Name of the Mumble server/channel")
    )
    url = models.CharField(
        max_length=255,
        validators=[validate_mumble_url],
        help_text=_("URL to the channel"),
    )

    class Meta:  # pylint: disable=too-few-public-methods
        """
        Meta definitions
        """

        default_permissions = ()
        verbose_name = _("Mumble Link")
        verbose_name_plural = _("Mumble Links")

    def __str__(self) -> str:
        return self.name
