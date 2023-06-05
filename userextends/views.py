from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.generic import CreateView
from userextends.forms import UserForm, AuthenticationNewForm

class UserCreateView(CreateView):
    template_name = 'userexentends/create_user.html'
    model = User
    form_class = UserForm

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.first_name = new_user.first_name.title()
        new_user.last_name = new_user.last_name.title()
        new_user.username = f'{new_user.first_name.lower()}{new_user.last_name.lower()}'

        if User.objects.filter(username=new_user.username).exists():
            return render(self.request, 'userexentends/error.html', {'error_message': 'Username already exists'})

        new_user.save()

        details = {
            'fullname': f'{new_user.first_name} {new_user.last_name}',
            'username': new_user.username
        }
        subject = 'New account!'
        message = render_to_string('mail.html', details)
        mail = EmailMessage(
            subject=subject,
            body=message,
            from_email=EMAIL_HOST_USER,
            to=[new_user.email]
        )
        mail.content_subtype = 'html'
        mail.send()

        return redirect('homepage')

class UserLoginView(LoginView):
    template_name = 'userexentends/login.html'
    authentication_form = AuthenticationNewForm
