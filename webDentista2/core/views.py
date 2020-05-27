  
#from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render
# Create your views here.
"""
Inicio home/
Historia about/
Servicios services/
Visítanos store/
Contacto contact/
Blog blog/
Sample sample/
"""

class HomePageView(TemplateView):
    """ count = User.objects.count()
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits +1
    return render(request, "core/home.html", {
       'count': count
    }) """

    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        count = User.objects.count()
        return render(request, self.template_name, {'count': count})


class AboutPageView(TemplateView):
    template_name = "core/about.html"

    def get(self, request, *args, **kwargs):
        count = User.objects.count()
        return render(request, self.template_name, {'count': count})

class StorePageView(TemplateView):
    template_name = "core/store.html"
    def get(self, request, *args, **kwargs):
        count = User.objects.count()
        return render(request, self.template_name, {'count': count})

class LoginPageView(TemplateView):
    template_name = "registration/login.html"
    def get(self, request, *args, **kwargs):
        count = User.objects.count()
        return render(request, self.template_name, {'count': count})

class Password_change_form_PageView(TemplateView):
    template_name = "registration/password_change_form.html"
    def get(self, request, *args, **kwargs):
        count = User.objects.count()
        return render(request, self.template_name, {'count': count})

class AccountPageView(TemplateView):
    template_name = "core/account.html"
    def get(self, request, *args, **kwargs):
        count = User.objects.count()
        return render(request, self.template_name, {'count': count})

class SignupPageView(TemplateView):
    template_name = "registration/signup.html"
    def get(self, request, *args, **kwargs):
        count = User.objects.count()
        return render(request, self.template_name, {'count': count})

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid(): 
#             form.save()
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/signup.html', {
#         'form': form
#     })





