"""
Test auth_hooks
"""

# Standard Library
from http import HTTPStatus

# Django
from django.test import TestCase
from django.urls import reverse

# Alliance Auth (External Libs)
from app_utils.testing import create_fake_user


class TestHooks(TestCase):
    """
    Test the app hook into allianceauth
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up groups and users

        :return:
        :rtype:
        """

        super().setUpClass()

        # User
        cls.user_1001 = create_fake_user(
            character_id=1001,
            character_name="Jean Luc Picard",
            permissions=[
                "aa_mumble_quick_connect.basic_access",
                "mumble.access_mumble",
            ],
        )

        cls.user_1002 = create_fake_user(
            character_id=1002, character_name="Wesley Crusher"
        )

        cls.html_menu = f"""
            <li class="d-flex flex-wrap m-2 p-2 pt-0 pb-0 mt-0 mb-0 me-0 pe-0">
                <i class="nav-link fa-solid fa-headphones-simple fa-fw align-self-center me-3 "></i>
                <a class="nav-link flex-fill align-self-center me-auto" href="{reverse('aa_mumble_quick_connect:index')}">
                    Mumble Quick Connect
                </a>
            </li>
        """

    def login(self, user):
        """
        Login a test user

        :param user:
        :type user:
        :return:
        :rtype:
        """

        self.client.force_login(user=user)

    def test_render_hook_success(self):
        """
        Test should show the link to the app

        :return:
        :rtype:
        """

        self.login(user=self.user_1001)

        response = self.client.get(path=reverse(viewname="authentication:dashboard"))

        self.assertEqual(first=response.status_code, second=HTTPStatus.OK)
        self.assertContains(response=response, text=self.html_menu, html=True)

    def test_render_hook_fail(self):
        """
        Test should not show the link to the app

        :return:
        :rtype:
        """

        self.login(user=self.user_1002)

        response = self.client.get(path=reverse(viewname="authentication:dashboard"))

        self.assertEqual(first=response.status_code, second=HTTPStatus.OK)
        self.assertNotContains(response=response, text=self.html_menu, html=True)
