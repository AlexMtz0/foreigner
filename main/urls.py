from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:casa_id>', views.mostrar_casa, name="casa_id"),
    path('crear/', views.crear_casa, name="crear_casa"),
    path('disponibles/', views.disponibles_casa, name="disponibles_casa"),
    path('propiedades/', views.propiedades_casa, name="propiedades_casa"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
