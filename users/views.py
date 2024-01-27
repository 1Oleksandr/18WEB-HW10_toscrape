from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
# from django.contrib.auth.decorators import login_required

from .forms import RegisterForm

# Create your views here.


class RegisterView(View):
    form_class = RegisterForm
    template_name = 'users/signup.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect(to='quotes:root')
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid:
            print(form)
            form.save()
            username = form.cleaned_data['username']
            messages.success(
                request, f'Account for {username} created successfully')
            return redirect(to='users:login')
        return render(request, self.template_name, {'form': form})

