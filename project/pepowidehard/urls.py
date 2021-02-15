from django.urls import path
from . import views
#static imports
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index),
    path('galery', views.galery_view),
    path('data', views.data_view),
    path('buzzing', views.buzzer_button, name="script"),
]
