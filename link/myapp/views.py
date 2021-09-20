from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework import status
from .utils import check_url
from .models import Link


class ShortLink(APIView):
    def post(self, request):
        try:
            data = request.data
            if "url" not in data.keys():
                return Response({
                    "success": False,
                    "message": "Request is not completed",
                    "detail": {"url": "Required field"}
                }, status=status.HTTP_400_BAD_REQUEST)

            if not check_url(data["url"]):
                return Response({
                    "success": False,
                    "message": "HTTP URL is not valid",
                    "detail": {"url": "Should be valid HTTP url"}
                }, status=status.HTTP_400_BAD_REQUEST)

            link = Link.objects.create(url=data["url"])
            return Response({
                "success": True,
                "message": "Short URL generated",
                "detail": {"result": f"http://127.0.0.1:8000/{link.short}"}
            }, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({
                "success": False,
                "message": "Internal server error",
                "detail": {}
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RedirectLink(APIView):
    def get(self, request, short):
        try:
            link = Link.objects.filter(short=short).first()
            if link is None:
                return Response({
                    "success": False,
                    "message": "No link found",
                    "detail": {"short": "No link found"}
                }, status=status.HTTP_404_NOT_FOUND)
            return HttpResponseRedirect(redirect_to=link.url)
        except:
            return Response({
                "success": False,
                "message": "Internal server error",
                "detail": {}
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)