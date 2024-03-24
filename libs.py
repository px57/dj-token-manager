
from token_manager.models import TokenModels
from django.apps import apps
from django.utils import timezone
import random

def generate_token(_in):
    """
    Generate a token

    Args:
        _in: The interface object
    """
    max_size = _in.token_max_size
    token_character_list = _in.token_character_list
    token = ''.join(random.choice(token_character_list) for i in range(max_size))
    return token

def create_token(_in, relatedModelId=None):
    """
    Create a token and save it in the database
    Args:
        _in: The interface object
        relatedModelId: The id of the related model
    """
    max_size = _in.token_max_size
    relatedModel = _in.relatedModel

    if relatedModelId is None:
        relatedModelId = _in.create_token__get_relatedModelId()

    token = generate_token(_in)
    dbToken = TokenModels.objects.create(
        token=token,
        relatedModel=relatedModel,
        relatedModelId=relatedModelId
    )
    return dbToken

def find_token(token):
    """
        @description: Va chercher dans la base de donne le token en question et seulement le token. 
        @params.token: The token that will be used to get the token object
    """
    try:
        dbToken = TokenModels.objects.get(token=token)
        return dbToken
    except TokenModels.DoesNotExist:
        return None
    
class RelatedObjectResponse(object):
    """
        @description: 
    """
    def __init__(self, token):
        """
            @description: 
        """
        self.__expire_after = None
        self.__token = token
        self.__dbToken = find_token(token=token)

    def set_expire_after(self, expire_after_time):
        """
            @description:
        """
        self.__expire_after = expire_after_time
        return self

    def has_expired_token(self):
        """
            @description: 
        """
        if self.__expire_after is None:
            return False
        
        now = timezone.now()
        if self.__dbToken.created_on + self.__expire_after < now:
            return True
        return False;

    def __get_model(self, model_path):
        """
            @description: get the model class with string.
        """
        if self.has_expired_token():
            return None
        
        model = apps.get_model(model_path)
        return model

    def get_relatedobject(self):
        """
            @description: 
        """
        self.__get_model(self.__dbToken.relatedModel)
        relatedObject = self.__get_model(self.__dbToken.relatedModel).objects.get(id=self.__dbToken.relatedModelId)
        return relatedObject

def get_relatedobject_totoken(token, expire_after_time=None):
    """
        @description: ont passe un token et ont retourne l'objet qui est lier au token, ou None
        @params.token: The token that will be used to get the token object
        @params.expire_after_time: The timedelta after the token will expire
    """
    relatedObjectResponse = RelatedObjectResponse(token=token)
    if expire_after_time is not None:
        relatedObjectResponse.set_expire_after(expire_after_time)
    return relatedObjectResponse 

def use_token(token):
    """
        @description: 
    """
    dbToken = find_token(token=token)
    if dbToken is None:
        return None
    
    dbToken.delete()
    return True

def redirect(_in):
    """
    Redirect the user to the right page
    """

def token_exists(token):
    """
        @description: Verify if the token exists. 
    """
    dbToken = find_token(token=token)
    if dbToken is None:
        return False
    return True

def has_expired_token(_in, dbToken):
    """
    Observe if the token is expired.
    """
