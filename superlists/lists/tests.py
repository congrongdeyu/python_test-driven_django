from django.test import TestCase


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        """
        Test that the home page is using the correct template
        """
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")
