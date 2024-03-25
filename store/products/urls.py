
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # path('catalog', views.products),
    # path('', views.index),
    path('user', views.user),
    path('basket', views.basket)
]

if settings.DEBUG:
    urlpatterns == static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)