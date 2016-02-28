from rest_framework.views import APIView
from rest_framework.response import Response

import re


class HomeAPIView(APIView):

    def get(self, request, format=None):
        context = dict()
        meta_keywords = [
            "HTTP_USER_AGENT",
            "HTTP_REFERER",
            "HTTP_HOST",
        ]

        for meta_keyword in meta_keywords:
            context[meta_keyword] = request.META.get(meta_keyword, None)

        # GET/POST Parameters
        context["GET"] = request.GET
        context["POST"] = request.POST

        # Full URL
        context["URL"] = request.build_absolute_uri()

        return Response(context)
