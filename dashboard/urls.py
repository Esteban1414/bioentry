from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('estadisticas/', views.estadisticas_view, name='estadisticas'),
    path('historial/', views.historial_view, name='historial'),
    path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
]

