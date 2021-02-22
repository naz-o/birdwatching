from django.urls import path
from . import views
#static imports
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index),
    path('galery', views.galery_view),
    path('data', views.data_view),
    path('getdatatemp', views.getdatatemp),
    path('getdatahum', views.getdatahum),
    path('buzzing', views.buzzer_button),
    path('getdatatempavg', views.getdatatempavg),
    path('getdatahumavg', views.getdatahumavg)
    #path('B')
]
