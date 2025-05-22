from django.urls import path
from .views import *

urlpatterns = [
    path('inventory/items/',InventoryList.as_view(),name='item_list'),
    path('inventory/items/<int:pk>/',InventoryDetails.as_view(),name='item_detail'),
    path('items/query/<str:category>/',InventoryQuery.as_view(),name='item_query'),
    path('items/sort/',InventorySort.as_view(),name='item_sort'),
    
]