from timeit import default_timer
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from .models import Product, Order, Author
from .forms import ProductForm, OrderForm, GroupForm


class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    fields = ["name"]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form=form)

class ShopIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        products = [
            ('Laptop', 1999),
            ('Desktop', 2999),
            ('Smartphone', 999),
        ]
        context = {
            'time_running': default_timer(),
            'products': products,
        }
        return render(request, 'shopapp/shop-index.html', context=context)

class GroupsListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "form": GroupForm(),
            'groups': Group.objects.prefetch_related('permissions').all(),
        }
        return render(request, 'shopapp/groups-list.html', context=context)

    def post(self, request: HttpRequest):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect(request.path)


class ProductDetailsView(DetailView):
    template_name = 'shopapp/product-details.html'
    model = Product
    context_object_name = "product"


class ProductsListView(ListView):
    template_name = 'shopapp/products-list.html'
    # model = Product
    context_object_name = "products"
    queryset = Product.objects.filter(archived=False)


# def create_order(request: HttpRequest) -> HttpResponse:
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             # name = form.cleaned_data['name']
#             # price = form.cleaned_data['price']
#             # Product.objects.create(**form.cleaned_data)
#             form.save()
#             url = reverse("shopapp:orders_list")
#             return redirect(url)
#     else:
#         form = OrderForm()
#     context = {
#         "form": form,
#     }
#
#     return render(request, "shopapp/order_form.html", context=context)


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('shopapp:orders_list')

class OrderUpdateView(UpdateView):
    model = Order
    fields = "products", "user", "delivery_address", "promocode"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse("shopapp:order_detail", kwargs={"pk": self.object.pk})

class OrderCreateView(CreateView):
    model = Order
    fields = "products", "user", "delivery_address", "promocode"
    success_url = reverse_lazy("shopapp:orders_list")

class OrdersListView(LoginRequiredMixin, ListView):
    queryset = (Order.objects\
        .select_related('user')\
        .prefetch_related('products'))

class OrderDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "shopapp:view_order"
    queryset = (Order.objects\
        .select_related('user')\
        .prefetch_related('products'))




class ProductUpdateView(PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    permission_required = ["shopapp:change_product",]
    def test_func(self):
        item = self.get_object()
        if self.request.user == item.created_by:
            return True
        return self.request.user.is_superuser
    model = Product
    fields = "name", "price", "description", "discount"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse("shopapp:product_details", kwargs={"pk": self.object.pk})

class ProductCreateView(PermissionRequiredMixin, UserPassesTestMixin, CreateView):
    permission_required = "shopapp:add_product"
    def test_func(self):
        # return self.request.user.groups.filter(name="secret-group").exists()
        return self.request.user.is_superuser
    model = Product
    fields = "name", "price", "description", "discount"
    success_url = reverse_lazy("shopapp:products_list")

    def form_valid(self, form):
        self.object = form.save()
        self.object.created_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('shopapp:products_list')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)






