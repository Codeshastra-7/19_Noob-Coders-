from django.urls import path, include
from app.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', index, name="main"),
    path('scan/', scan, name="scan"),
    path('help/', help, name="help"),
    path('<int:id>/dashboard/' ,dashboard, name="dashboard"),
    path('<int:id>/distance/', location, name="distance"),
    path('<int:id>/wareupdate/', WareUpdate, name="warehousedetupdate"),
    path('<int:id>/qrgen/', qrgenerate, name="qrgen"),
    path('<int:id>/data/<int:qid>', qrdata, name="qrdata"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

