import os
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.urls import reverse_lazy

from .models import User
from .forms import UserForm


class LoginView(FormView):
    form_class = UserForm
    template_name = "index.html"
    success_url = reverse_lazy("accounts:success")
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        username = form.data["username"]
        password = form.data["password"]
        query = f"SELECT id, username FROM accounts_user WHERE username='{username}' AND password='{password}'"
        if len(User.objects.raw(query)) > 0:
            flag = os.getenv("FLAG", "")
            return render(request, "success.html", {"flag": flag})
        else:
            return redirect("/")
        
