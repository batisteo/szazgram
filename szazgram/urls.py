from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from api.views import JSONView, IllustrationViewSet

router = routers.DefaultRouter()
router.register(r'illustrations', IllustrationViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', JSONView.as_view()),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
