from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('item/', views.item_list, name='item_list'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('item/register/', views.item_register, name='item_register'),
    path('item/<int:pk>/update/', views.item_update, name='item_update'),
    path('item/<int:pk>/delete/', views.item_delete, name='item_delete'),
    path('account/', views.account_list, name='account_list'),
    path('account/<int:pk>/', views.account_detail, name='account_detail'),
    path('account/register/', views.account_register, name='account_register'),
    path('account/<int:pk>/update/', views.account_update, name='account_update'),
    path('account/<int:pk>/delete/', views.account_delete, name='account_delete'),
]