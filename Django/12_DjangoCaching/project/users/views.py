from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import UserCreationForm
from .models import Shop


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm(),
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context=context)

class ShopListView(ListView):
    template_name = 'shop.html'
    context_object_name = "shops"
    queryset = Shop.objects.all()