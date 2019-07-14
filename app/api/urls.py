from django.urls import path
from .views import SalesListAPIView

urlpatterns = [
    path('api/sales', SalesListAPIView.as_view()),
]
