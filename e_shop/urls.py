from django.urls import include, path
from rest_framework.routers import DefaultRouter

from e_shop.views import SupplierViewSet

router = DefaultRouter()

router.register(r"suppliers", SupplierViewSet, basename="suppliers")

app_name = "e_shop"

urlpatterns = [
    path("", include(router.urls)),
]
