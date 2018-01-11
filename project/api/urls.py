
from django.conf.urls import url, include
from rest_framework import routers
from project.api import views
router = routers.DefaultRouter()
router.register(r'userered', views.UserViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
]