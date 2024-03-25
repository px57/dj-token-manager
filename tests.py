from django.test import TestCase
from django.test import Client
from token_manager.libs import create_token, find_token, get_relatedobject_totoken
from gpm.http import Response
import profiles

class TokenTestUsage(TestCase):

    def test_create_token(self):
        """
            @description: 
        """
        token = create_token(
            max_size=32, 
            relatedModel='profiles.Profile', 
            relatedModelId=1
        )

    def test_getrelatedobject(self):
        """
            @description:
        """
        token = create_token(
            max_size=32, 
            relatedModel='profiles.Profile', 
            relatedModelId=1
        )
        
        try: 
            get_relatedobject_totoken(token=token.token)
        except Exception as e: 
            self.fail('Exception raised')

class RedirectWithToken(TestCase):
    """
        @description:
    """

    def test_create_redirect_url(self):
        """
            @description:
        """
        res = Response(request=None)
        token = create_token(
            max_size=32, 
            relatedModel='profiles.Profile', 
            relatedModelId=1
        )
        redirect_url = token.create_redirect_url(res)

    def test_use_redirect_url(self):
        """
            @description:
        """
        res = Response(request=None)
        token = create_token(
            max_size=32, 
            relatedModel='profiles.Profile', 
            relatedModelId=1
        )
        redirect_url = token.create_redirect_url(res)
        c = Client()
        response = c.get(redirect_url)