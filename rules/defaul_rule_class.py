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
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [END] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

TOKEN_MANAGER_RULESTACK.set_rule(DefaultRuleClass())