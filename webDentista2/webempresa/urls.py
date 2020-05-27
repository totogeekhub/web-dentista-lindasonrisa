"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import login
from pages.urls import pages_patterns
from profiles.urls import profiles_patterns
from messenger.urls import messenger_patterns

urlpatterns = [
    #paths del core
    path('', include('core.urls')),
    #paths de services
    path('services/', include('services.urls')),
    #paths de blog
    path('blog/', include('blog.urls')),
    #paths de pages
    path('pages/', include(pages_patterns)),
    #paths de contact
    path('contact/', include('contact.urls')),
    #Paths del admin
    path('admin/', admin.site.urls),
    #Paths del login
    #path('login/', admin.site.urls), 
    #Paths del signup
    #path('signup/', admin.site.urls),
    #path('account/', admin.site.urls),
    # Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    #('password_change_form/', admin.site.urls),
    # Paths de profiles
    path('profiles/', include(profiles_patterns)),
    # Paths de Messenger
    path('messenger/', include(messenger_patterns)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)