from django.db.models import Q
from django.contrib.postgres.search import TrigramSimilarity

from rest_framework import viewsets
from rest_framework.response import Response

from core.utils import remove_accents
from geofr.models import Perimeter
from geofr.api.serializers import PerimeterSerializer


MIN_SEARCH_LENGTH = 1


class PerimeterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PerimeterSerializer

    def get_queryset(self):
        """Filter data according to search query."""

        qs = Perimeter.objects.order_by('-scale', 'name')

        accented_q = self.request.query_params.get('q', '')
        q = remove_accents(accented_q)

        if len(q) >= MIN_SEARCH_LENGTH:
            qs = qs \
                .annotate(similarity=TrigramSimilarity('unaccented_name', q)) \
                .filter(Q(unaccented_name__trigram_similar=remove_accents(q))
                        | Q(zipcodes__icontains=accented_q)) \
                .order_by('-similarity', '-scale', 'name')

        is_visible_to_users = self.request.query_params.get('is_visible_to_users', 'false')
        if is_visible_to_users == 'true':
            qs = qs.filter(is_visible_to_users=True)

        return qs


class PerimeterScales(viewsets.ViewSet):
    """
    List all the perimeter scales.
    """

    def list(self, request):
        aid_steps = [{'key': key, 'value': value} for (key, value) in Perimeter.SCALES]
        data = {
            'count': len(aid_steps),
            'results': aid_steps
        }
        return Response(data)
