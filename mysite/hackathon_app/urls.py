from rest_framework.urls import path
from .views import *


urlpatterns = [
    path('user/', UserProfileAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserProfileEditAPIView.as_view(), name='user_edit'),

    # category
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    # path('category/create/', .as_view(), name=''),
    # path('', .as_view(), name=''),
    # path('', .as_view(), name=''),
    # path('', .as_view(), name=''),
    # path('', .as_view(), name=''),
    # path('', .as_view(), name=''),
    # path('', .as_view(), name=''),
    # path('', .as_view(), name=''),
    # path('', .as_view(), name=''),
]

