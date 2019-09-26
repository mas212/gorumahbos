from django.urls import path
from . import views
app_name ='categories'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('store', views.store, name='store'),
    path('edit/<int:cat_id>', views.edit, name='edit'),
    path('update/<int:cat_id>', views.update, name='update'),
    path('delete/<int:cat_id>', views.delete, name='delete'),
]