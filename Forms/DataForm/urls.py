from django.urls import path
from . import views
urlpatterns=[
    path('store/',views.data_stroe,name='data_store'),
]
