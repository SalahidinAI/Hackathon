from rest_framework.urls import path
from .views import *


urlpatterns = [
    path('user/', UserProfileAPIView.as_view(), name='user_list'),
    # path('', .as_view(), name=''),
    # path('', .as_view(), name=''),
    # path('', .as_view(), name=''),
    # path('', .as_view(), name=''),
    # path('', .as_view(), name=''),
    # path('', .as_view(), name=''),
    # path('', .as_view(), name=''),
    # path('', .as_view(), name=''),
    # path('', .as_view(), name=''),
]

