from django.conf.urls import include, url
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)

#router.register(r'basic-data/tracing', bd_views.TracingViewSet, basename="bd_tracing")

urlpatterns = [
    url(r'^', include(router.urls)),
]
