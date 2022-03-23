from django.urls import path
from . import views

urlpatterns = [
    path('add_workorder', views.add_workorder, name='add-workorder'),
    path('workorders', views.all_workorders, name='list-workorders'),
    path('workorder_detail/<workorder_id>', views.workorder_detail, name='workorder-detail'),
    path('update_workorder/<workorder_id>', views.workorder_update, name='workorder-update'),
]
