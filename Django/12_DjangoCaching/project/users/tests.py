
from django.test import TestCase
from django.urls import reverse
from .models import Shop, Profile, User


class ShopListViewTestCase(TestCase):
    def test_shop_list_view(self):
        response = self.client.get(reverse("shop"))
        self.assertEqual(response.status_code, 200)


class HomeViewTestCase(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)


class RegisterViewTestCase(TestCase):
    def test_register_view(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

# class RegisterViewRedirectTestCase(TestCase):
#     def test_redirect_register_view(self):
#         response = self.client.post(reverse('register'), {
#             'username': 'username',
#             'password': 'password1'
#         })
#         self.assertRedirects(response, reverse('home'))


class ShopPageContentTestCase(TestCase):
    def test_shop_page_content(self):
        response = self.client.get(reverse('shop'))
        for shop in Shop.objects.all():
            self.assertContains(response, shop.name)



class HomePageContentTestCase(TestCase):

    def setUp(self) -> None:
        self.user = Profile.objects.create()

    def tearDown(self) -> None:
        self.user.delete()

    def test_home_page_content(self):

        response = self.client.get(reverse('home'))

        self.assertContains(response, self.user.balance)
        self.assertContains(response, self.user.promo)
        self.assertContains(response, self.user.offers)



