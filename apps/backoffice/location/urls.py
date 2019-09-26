from django.urls import path
from . import views
app_name ='location'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('store', views.store, name='store'),
    path('edit/<int:location_id>', views.edit, name='edit'),
    path('update/<int:location_id>', views.update, name='update'),
    path('delete/<int:location_id>', views.delete, name='delete')
]