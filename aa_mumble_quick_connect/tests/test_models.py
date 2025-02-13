# Django
from django.conf import settings
from django.core.exceptions import ValidationError
from django.test import TestCase, override_settings

# AA Mumble Quick Connect
from aa_mumble_quick_connect.models import MumbleLink, Section, validate_mumble_url


class TestSection(TestCase):
    """
    Tests for the `Section` model
    """

    def test_model_string_names(self):
        """
        Test model string name

        :return:
        :rtype:
        """

        section = Section(name="Foobar")
        section.save()
        expected_name = section.name
        self.assertEqual(first=str(section), second=expected_name)


class TestMumbleLink(TestCase):
    """
    Tests for the `MumbleLink` model
    """

    def test_model_string_names(self):
        """
        Test model string name

        :return:
        :rtype:
        """

        section = MumbleLink(name="Foobar")
        section.save()
        expected_name = section.name
        self.assertEqual(first=str(section), second=expected_name)

    @override_settings(MUMBLE_URL="mumble.example.com")
    def test_validate_mumble_url_with_valid_url(self):
        """
        Test validate Mumble URL with valid URL

        :return:
        :rtype:
        """

        expected_mumble_base_url = f"mumble://{settings.MUMBLE_URL}"

        self.assertEqual(
            first=validate_mumble_url(url=f"mumble://{settings.MUMBLE_URL}"),
            second=expected_mumble_base_url,
        )

    @override_settings(MUMBLE_URL="mumble.example.com")
    def test_validate_mumble_url_with_invalid_url(self):
        """
        Test validate Mumble URL with invalid URL

        :return:
        :rtype:
        """

        expected_mumble_base_url = f"mumble://{settings.MUMBLE_URL}"

        with self.assertRaisesMessage(
            expected_exception=ValidationError,
            expected_message=f"The Mumble channel URL must start with '{expected_mumble_base_url}'",
        ):
            validate_mumble_url("http://example.com")
