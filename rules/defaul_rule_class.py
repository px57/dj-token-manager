from token_manager.rules.stack import TOKEN_MANAGER_RULESTACK
from kernel.interfaces.interfaces import InterfaceManager
from datetime import timedelta

# TODO: Deja il faut integrer ce code a l'ensemble des endroits ou il y a des regles.

class DefaultRuleClass(InterfaceManager):
    """
        @description: The default rule class.
    """

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [EXPIRE] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    """
        @description: The token expiration allow.
    """
    token_expiration_allow = False

    """
        @description: The token expiration after.
    """
    expiration_after = timedelta(days=1)

    """
    token max size
    """
    token_max_size = 32

    """
    token min size
    """
    token_min_size = 32

    """
    Token character list 
    """
    token_character_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    """
    Related model   
    """
    relatedModel = None

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [END] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def create_token__get_relatedModelId(self):
        """
        Get the related model id, from the request.
        """
        if self.request.method == 'GET':
            return self.request.GET.get('relatedModelId')
        return self.request.POST.get('relatedModelId')
    
    def event_token_expired(self):
        """
        Run this event when the token is expired.
        """

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [CHECK] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def gpm__viewparams__check_is_valid(self):
        """
        Check if the token is valid.
        """
        return {
            'token': self.request.POST.get('token')
        }

    def event_check_token(self, dbToken):
        """
        Check the token, and mark it as used.

        Args:
            dbToken (TokenModel): The token
        Return: 
            dbToken (TokenModel): The token
        """
        dbToken.is_active = False
        dbToken.save()
        return dbToken

class NumericRuleClass(DefaultRuleClass):
    """
    The numeric rule class.
    """
    token_character_list = '0123456789'

class DigitalNumericRuleClass(DefaultRuleClass):
    """
    The digital numeric rule class.
    """
    token_character_list = '0123456789'
    token_max_size = 4
        
# TOKEN_MANAGER_RULESTACK.set_rule(DefaultRuleClass)