# Django
from django.test import TestCase

# AA Mumble Quick Connect
from aa_mumble_quick_connect.models import MumbleLink, Section


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
