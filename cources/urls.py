from django.urls import path
from . import views

app_name = 'cources'

urlpatterns = [
    path('/cource/list', views.CourceListView.as_view(), name='cource_list'),
    path('/cource/create', views.CourceCreateView.as_view(), name='cource_create'),
    path('/cource/update/<int:pk>', views.CourceUpdateView.as_view(), name='update_cource'),
    path('/cource/delete/<int:pk>', views.DeleteView, name='delete_cource'),
]