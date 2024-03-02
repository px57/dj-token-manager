
from django.shortcuts import render
from kernel.http import Response 
from token_manager.libs import create_token as create_token_lib
from token_manager.libs import find_token as find_token_lib
from token_manager.libs import use_token as use_token_lib
from token_manager.libs import token_exists as token_exists_lib
from token_manager.libs import redirect as redirect_lib
from profiles.decorators import load_profile
from kernel.http import load_response
from token_manager.rules.stack import TOKEN_MANAGER_RULESTACK

@load_profile
@load_response(stack=TOKEN_MANAGER_RULESTACK)
def create_token(request, res=None):
    """
        @description: 
    """
    _in = res.get_interface()
    relatedModelId = _in.create_token__get_relatedModelId()

    dbToken = create_token_lib(_in)
    res.token = dbToken.serialize(request)
    return res.success()

@load_profile
@load_response(stack=TOKEN_MANAGER_RULESTACK)
def redirect(request, token, res=None):
    """
        @description: 
    """
    return res.success()

# @load_profile
# @load_response(stack=TOKEN_MANAGER_RULESTACK)
# def token_exists(request, res=None):
#     """
#         @description: Verify if the token exists. 
#     """
#     return res.success()

# @load_profile
# @load_response(stack=TOKEN_MANAGER_RULESTACK)
# def use_token(request, res=None):
#     """
#         @description: Use the token and delete it from the database
#     """
#     return res.success()
