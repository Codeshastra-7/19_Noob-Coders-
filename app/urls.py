from django.urls import path, include
from app.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name="main"),
    path('<int:id>/dashboard/' ,dashboard, name="dashboard"),
    path('<int:id>/distance/', location, name="distance"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

