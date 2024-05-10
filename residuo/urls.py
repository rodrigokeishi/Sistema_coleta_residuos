from django.urls import path, include
from .views import homepage, homeresiduos

urlpatterns = [
    path('', homepage),
    path('residuos/', homeresiduos),
]