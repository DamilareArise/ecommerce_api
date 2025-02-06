from django.urls import path
from .views import ProductView

urlpatterns = [
    path('get-product/', ProductView.as_view())
]
 