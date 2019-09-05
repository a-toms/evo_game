from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
import sys
sys.path.insert(1, '/source/evo_app/')
from evo_app import views

router = routers.DefaultRouter()
router.register(r'players', views.PlayerView, 'player')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]