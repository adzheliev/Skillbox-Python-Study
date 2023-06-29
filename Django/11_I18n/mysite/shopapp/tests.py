from string import ascii_letters
from random import choices

from django.contrib.auth.models import User, Permission
from django.test import TestCase
from django.urls import reverse

from shopapp.models import Product, Order, Product
from shopapp.utils import add_two_numbers
from django.conf import settings
from django.test import Client


class AddTwoNumbersTestCase(TestCase):
    def test_add_two_numbers(self):
        result = add_two_numbers(2, 3)
        self.assertEqual(result, 5)

class ProductCreateViewTestCase(TestCase):
    def setUp(self) -> None:
        self.product_name = "".join(choices(ascii_letters, k=10))
        Product.objects.filter(name=self.product_name).delete()

    def test_create_product(self):
        response = self.client.post(reverse("shopapp:product_create"),
                         {
                             "name": self.product_name,
                             "price": "123.45",
                             "description": "A good table",
                             "discount": "10"

                         })
        self.assertRedirects(response, reverse("shopapp:products_list"))
        self.assertTrue(Product.objects.filter(name=self.product_name).exists())


class ProductDetailsViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.product = Product.objects.create(name="Best Product")

    # def setUp(self) -> None:
    #     self.product = Product.objects.create(name="Best Product")

    @classmethod
    def tearDownClass(cls):
        cls.product.delete()

    # def tearDown(self) -> None:
    #     self.product.delete()

    def test_get_product(self):
        response = self.client.get(reverse("shopapp:product_details", kwargs={"pk": self.product.pk}))
        self.assertEqual(response.status_code, 200)

    def test_get_product_and_check_content(self):
        response = self.client.get(reverse("shopapp:product_details", kwargs={"pk": self.product.pk}))
        self.assertContains(response, self.product.name)

class ProductListViewTestCase(TestCase):
    fixtures = [
        "products-fixture.json"
    ]
    def test_product(self):
        response = self.client.get(reverse("shopapp:products_list"))
        # for product in Product.objects.filter(archived=False).all():
        #     self.assertContains(response, product.name)
        products = Product.objects.filter(archived=False).all()
        products_ = response.context["products"]
        # for p, p_ in zip(products, products_):
        #     self.assertEqual(p.pk, p_.pk)
        self.assertQuerysetEqual(
            qs=Product.objects.filter(archived=False).all(),
            values=(p.pk for p in response.context["products"]),
            transform=lambda p: p.pk
        )
        self.assertTemplateUsed(response, 'shopapp/products-list.html')


class OrdersListViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.credentials = dict(username="bob_test", password="qwerty")
        cls.user = User.objects.create_user(username="bob_test", password="qwerty")

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
    def setUp(self) -> None:
        # self.client.login(**self.credentials)
        self.client.force_login(self.user)
    def test_orders_view(self):
        response = self.client.get(reverse("shopapp:orders_list"))
        self.assertContains(response, "Orders")

    def test_orders_view_not_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse("shopapp:orders_list"))
        # self.assertRedirects(response, str(settings.LOGIN_URL))
        self.assertEqual(response.status_code, 302)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class ProductExportViewTestCase(TestCase):
    fixtures = [
        "products-fixture.json"
    ]

    def test_get_products_view(self):
        response = self.client.get(
            reverse("shopapp:products-export")
        )
        self.assertEqual(response.status_code, 200)
        products = Product.objects.order_by("pk").all()
        expected_data = [
            {
                "pk": product.pk,
                "name": product.name,
                "price": str(product.price),
                "archived": product.archived,
            }
            for product in products
        ]
        products_data = response.json()
        self.assertEqual(products_data["products"], expected_data)


class OrderDetailViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="bob_test", password="qwerty", email="test@test.ru")


    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        codenames = ['add_order', 'change_order', 'view_order']
        for codename in codenames:
            permission = Permission.objects.get(codename=codename,)
            self.user.user_permissions.add(permission)
        self.client.force_login(self.user)
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
        self.order = Order(user=self.user, delivery_address="Pupkina st.5", promocode="skillbox")
        self.order.save()

    def tearDown(self) -> None:
        self.order.delete()

    def test_profile_page_show_correct_context(self):
        response = self.authorized_client.get(reverse("shopapp:order_detail", kwargs={"pk": self.order.pk}))
        self.assertContains(response, self.order.pk)

    def test_order_details(self):
        self.assertEqual("Pupkina st.5", self.order.delivery_address)
        self.assertEqual("skillbox", self.order.promocode)

class OrderExportTestCase(TestCase):

    @classmethod
    def setUpClass(cls):

        fixtures = [
            "orders-fixture.json",
        ]

        cls.user = User.objects.create_user(username="bob_test",
                                            password="qwerty",
                                            email="test@test.ru",
                                            is_staff=True)
    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_get_products_view(self):
        response = self.client.get(
            reverse("shopapp:orders-export")
        )
        self.assertEqual(response.status_code, 200)
        orders = Order.objects.order_by("pk").all()
        expected_data = [
            {
                "pk": order.pk,
                "delivery_address": order.delivery_address,
                "promocode": order.promocode,
                "user": order.user,
                "products": order.products.all()
            }
            for order in orders
        ]
        orders_data = response.json()
        self.assertEqual(orders_data["orders"], expected_data)
