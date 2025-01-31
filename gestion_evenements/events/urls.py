from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('new/', views.event_create, name='event_create'),
    path('<int:event_id>/edit/', views.event_update, name='event_update'),
    path('<int:event_id>/delete/', views.event_delete, name='event_delete'),
    path('<int:event_id>/join/', views.join_event, name='join_event'),
    path('<int:event_id>/leave/', views.leave_event, name='leave_event'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
