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
        
TOKEN_MANAGER_RULESTACK.set_rule(DefaultRuleClass())