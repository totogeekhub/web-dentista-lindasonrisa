from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.shortcuts import render, get_object_or_404
from .models import Service, Category
# Create your views here.

class ServicesPageView(TemplateView):
    template_name = "services/services.html"

    def get(self, request, *args, **kwargs):
        services = Service.objects.all()
        count = User.objects.count()
        return render(request, self.template_name, {'services': services, 'count': count,})


""" class CategoryPageView(TemplateView):
    template_name = "services/category.html"

    def get(self, request, *args, **kwargs):
        categories = get_object_or_404(Category, id=category_id)
        return render(request, self.template_name, {'categories': categories}) """

""" def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, "services/category.html", {'category':category})
 """
