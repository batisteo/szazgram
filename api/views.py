from django.views.generic import TemplateView
from rest_framework import viewsets

from .models import Illustration
from .serializers import IllustrationSerializer
from .mixins import JSONResponseMixin
from .utils import load_csv


class IllustrationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows illustrations to be viewed or edited.
    """
    queryset = Illustration.objects.all().order_by('title')
    serializer_class = IllustrationSerializer

    def list(self, request):
        load_csv()
        return super().list(request)


class JSONView(JSONResponseMixin, TemplateView):
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)

    def get_data(self, context):
        context = {'url': 'who cares...'}
        return super().get_data(context)
