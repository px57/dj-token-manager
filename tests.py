from django.test import TestCase
from token_manager.libs import create_token, find_token, get_relatedobject_totoken
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
            print ('Exception: ', e)
        # self.assertRaises(, )

# TODO: Test use token
