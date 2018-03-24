from django.urls import path
from .import views

urlpatterns = [
    path('add', views.insert_data, name="insert_data"),
    path('del', views.del_data, name="del_data"),
    path('update', views.up_date, name="up_date"),
    path('get', views.get_data, name="get_data"),
    path('active/<int:id>', views.active, name="active"),
    path('unactive/<int:id>', views.un_active, name="un_active"),
    # path('cn/<str:name>/<int:status>', views.n_change_status, name="n_change_status"),
    # path('time/', views.get_time),
]