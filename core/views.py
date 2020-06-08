from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.serializers import UserSerializer
from django.http import HttpResponse
from core.scraper.google import GoogleAnalysis
from core.scraper.facebook import FacebookAnalysis
from core.scraper.instagram import InstagramAnalysis


class SearchView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        word = request.data['keyword']
        facebook = []
        instagram = []
        google = []
        if request.data['instagram']:
            instagram = InstagramAnalysis(word)
            instagram = instagram.run()

        if request.data['facebook']:
            facebook = FacebookAnalysis(word)
            facebook = facebook.run()


        
        google = GoogleAnalysis(word)
        google = google.run()

        return Response({"google": google, "facebook": facebook, "instagram": instagram})


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = UserSerializer(request.user)
        print(user.data)
        return Response(user.data)

