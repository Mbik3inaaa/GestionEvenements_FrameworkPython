from django.contrib import admin
from django.urls import path, include
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('events/', include('events.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # 🔥 Ajoute ceci pour gérer login/logout
    
]
