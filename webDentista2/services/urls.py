from django.urls import path
from .views import ServicesPageView#, CategoryPageView

urlpatterns = [
    #Paths del services
    path('', ServicesPageView.as_view(), name="services"),
    #path('category/<int:category_id>/', CategoryPageView.as_view(), name="category"),
]