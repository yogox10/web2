from django.urls import path
from Fam.views import familia, adicional, api_familia, buscar_pariente


urlpatterns = [
    path ('familia/', familia),
    path ('adicional/', adicional),
    path ('api_familia/', api_familia),
    path ('buscar_pariente/', buscar_pariente)
 ] 