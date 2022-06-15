from django.urls import path
from . import views

urlpatterns = [
    path('Import_csv',views.Import_csv,name="Import_csv"),
    path('chart',views.charts,name='charts'),
    path('data',views.data,name='data')
]
