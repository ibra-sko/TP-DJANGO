"""
URL configuration for ConcessionAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from concession_api.routers import concession_router, router
from django.http import JsonResponse

def root_view(request):
    return JsonResponse({"message": "Bienvenue sur l'API Concession. Visitez /api/concessions pour commencer."})

urlpatterns = [
    path('', root_view),  # Vue pour la route racine
    path('api/', include(router.urls)),  # Routes de base pour API
    path('api/', include(concession_router.urls)),  # Routes imbriquées
]

