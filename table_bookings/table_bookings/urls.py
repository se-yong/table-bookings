from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('web.urls')),
    path('office/', include('office.urls')),
    path('admin/', admin.site.urls),
    path('oauth/', include('allauth.urls')),
    path('prometheus/', include('django_prometheus.urls'))
]
