from django.views.generic import TemplateView
from rest_framework import viewsets

from .models import Illustration
from .serializers import IllustrationSerializer


class IllustrationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows illustrations to be viewed or edited.
    """
    queryset = Illustration.objects.all().order_by('title')
    serializer_class = IllustrationSerializer
