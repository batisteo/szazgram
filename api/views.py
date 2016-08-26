from django.conf import settings
from django.views.generic import TemplateView
from rest_framework import viewsets

from .models import Illustration
from .serializers import IllustrationSerializer
from .mixins import JSONResponseMixin
from .utils import fetch_csv, get_offline_csv


class IllustrationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows illustrations to be viewed or edited.
    """
    queryset = Illustration.objects.all().order_by('title')
    serializer_class = IllustrationSerializer


class JSONView(JSONResponseMixin, TemplateView):
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)

    def get_data(self, context):
        context = {'url': settings.DATA_URL}
        # fetch_csv(settings.DATA_URL)
        get_offline_csv('test_application_data.csv')
        return super().get_data(context)
