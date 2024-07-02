from django.urls import path
from . import views
from .views import get_posts

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<int:pk>/edit/', views.edit_product, name='edit_product'),  # URL for edit product
    path('<int:pk>/delete/', views.delete_product, name='delete_product'),  # URL for delete product
    path('get-posts/', get_posts, name='get_posts'),  # URL for API endpoint to get posts
]
