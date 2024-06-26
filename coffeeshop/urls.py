from django.urls import path
from .views import create_product, product_list, product_details, product_update

urlpatterns = [

    path("product-list/", product_list),
    path("create-product/", create_product),
    path("product-details/<int:id>/", product_details),
    path("product-update/<int:id>/", product_update),
]
