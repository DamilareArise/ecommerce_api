from django.urls import path, include
# from .views import ProductView
from .views import ProductViewSet
# from .views import createProduct
# from .views import productView
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     # path('product/<int:pk>/', ProductView.as_view()),
#     path('product/', ProductView.as_view()),
# ]
 
 
# using viewSet

router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')
urlpatterns = [
    path('', include(router.urls)),
]



# using genericApiView

# urlpatterns = [
#     # path('product/', createProduct.as_view()),
#     path('product/', productView.as_view()),
# ]
