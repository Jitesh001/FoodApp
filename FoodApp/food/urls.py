from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    #food/
    path('', views.indexClassView.as_view(), name='index'),
    #food/1
    #path('<int:itm_id>/', views.details, name = 'details'),
    path('<int:pk>/', views.FoodDetail.as_view(), name = 'details'),
    #form to add item
    #path("add/", views.add_item, name="add_item"),
    path("add/", views.AddItem.as_view(), name="add_item"),
    # #update item
    path('update/<int:itm_id>', views.update_item, name='update_item'), 
    #delete item
    path('delete/<int:itm_id>', views.delete_item, name='delete_item'), 
]