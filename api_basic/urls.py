from django.urls import path, include
from . views import ModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ModelViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    # path('article/', article_list),
    # path('article/', articleapiview.as_view()),
    # path('detail/<int:id>/', articledetails.as_view()),
    # path('generic/detail/<int:id>/', genericapiview.as_view()),
    # path('detail/<int:pk>/', article_detail),
]
