from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

# to implement a custom authentication scheme, subclass BASEAUTHENTICATION and override the authenticate(self,request) method
# the method should return a two tuple of (user,auth) if authentication succeeds, or NONE otherwise


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get('username')
        if username is None:
            return None

        try:
            user = User.objects.get(username=username)

        except User.DoesNotExist:
            raise AuthenticationFailed("No Such User")

        return (user, None)
