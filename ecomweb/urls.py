"""ecomweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from rest_framework import routers

from profiles import views as profiles_views, viewsapi
from contact import views as contact_views

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'users', viewsapi.UserViewSet)
router.register(r'groups', viewsapi.GroupViewSet)
router.register(r'category', viewsapi.CategoryViewSet)
router.register(r'product', viewsapi.ProductViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', profiles_views.home, name='home'),
    path('about/', profiles_views.about, name='about'),
    path('contact/', contact_views.contact, name='contact'),
    path('manage/', profiles_views.manage, name='manage'),
    path('<int:cat>/', profiles_views.home, name='categorys-ss'),
    path('api/', include(router.urls)),
    #url(r'^', include(routers.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
