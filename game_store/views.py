import logging

from django.core.paginator import Paginator

from .models import Game

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


logger = logging.getLogger(__name__)


class GamesView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'game_store/games.html'

    @staticmethod
    def get_category_id(request) -> str:
        """Performs validation on request parameter category_id

        Returns None if category_id parameter is missing or contains invalid
        info e.g negative value or chars other than [0-9]
        """
        try:
            category_id = request.GET.get('category_id', None)
            if category_id and int(category_id) >= 0:
                return category_id
        except Exception:
            logger.exception('An exception occurred'
                             ' while validating parameter category_id',
                             exc_info=True)

    @staticmethod
    def get_paginator_obj(queryset, request):
        """Paginates queryset"""
        paginator = Paginator(queryset, 3)  # Show 3 games per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return page_obj

    def get(self, request) -> Response:
        """Returns list of games filtered by category_id(when present)"""
        category_id = GamesView.get_category_id(request)

        try:
            if category_id:
                queryset = Game.objects.filter(category=category_id).order_by('id')
            else:
                queryset = Game.objects.all().order_by('id')
        except Exception:
            logger.exception('An exception occurred retrieving game records'
                             ' from model', exc_info=True)
            return Response("Internal server error",
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        paginated_games = GamesView.get_paginator_obj(queryset, request)
        return Response({'page_obj': paginated_games})
