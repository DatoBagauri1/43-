from django.urls import path
from .views import HelloView, CustomTokenObtainPairView, CustomTokenRefreshView

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
