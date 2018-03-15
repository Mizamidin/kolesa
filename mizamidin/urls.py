from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.CarListView.as_view(), name='cars'),
    path('car/<int:pk>', views.CarDetailView.as_view(), name='car-detail'),
    path('sellers/', views.SellerListView.as_view(), name='sellers'),
    path('seller/<int:pk>', views.SellerDetailView.as_view(), name='seller-detail'),
]
urlpatterns += [  
    path('seller/create/', views.SellerCreate.as_view(), name='seller_create'),
    path('seller/<int:pk>/update/', views.SellerUpdate.as_view(), name='seller_update'),
    path('seller/<int:pk>/delete/', views.SellerDelete.as_view(), name='seller_delete'),
]