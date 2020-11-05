from django.urls import path
from . import views
urlpatterns = [
    path('firstpgm', views.myfun,name='firstpgm'),
    path('secpgm', views.fun,name='secondtpgm'),
    path('sample',views.ff,name='sample'),
]