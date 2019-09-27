from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from . import views
app_name = 'listing'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('store', views.store, name='store'),
    path('delete/<int:listing_id>',views.delete, name='delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

