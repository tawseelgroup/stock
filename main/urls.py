from django.urls import reverse, path
from .views import  ItemDetailView
from . import views
urlpatterns = [
    path('', views.main, name='main'),
    # path('', MainView.as_view(), name='main'),
    path('item-details/<int:pk>', ItemDetailView.as_view(), name='getdetails'),
    path('new-item', views.newitem, name='newitem'),
    path('additem', views.additem, name='additem'),
    path('item/<int:id>/edit/', views.updatingform, name='updatingform'),
    # path('item/<int:pk>/edit/', views.update_item, name='update_item'),
]
