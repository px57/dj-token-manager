
from django.shortcuts import render
from kernel.http import Response 
from token_manager.libs import create_token as create_token_lib
from token_manager.libs import find_token as find_token_lib
from token_manager.libs import use_token as use_token_lib
from token_manager.libs import token_exists as token_exists_lib
from token_manager.libs import redirect as redirect_lib

from token_manager.rules.stack import TOKEN_MANAGER_RULESTACK

from token_manager.forms import CheckIsValidForm

from profiles.decorators import load_profile
from kernel.http import load_response


@load_profile
@load_response(stack=TOKEN_MANAGER_RULESTACK)
def create_token(request, res=None, _in=None):
    """
        @description: 
    """
    # _in = res.get_interface()
    relatedModelId = _in.create_token__get_relatedModelId()

    dbToken = create_token_lib(_in)
    res.token = dbToken.serialize(request)
    return res.success()

@load_profile
@load_response(stack=TOKEN_MANAGER_RULESTACK)
def redirect(request, token, res=None, _in=None):
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

@load_response(
    stack=TOKEN_MANAGER_RULESTACK,
    json=True,
    load_params=True,
    form=CheckIsValidForm
)
def check_is_valid(
    request, 
    res=None, 
    _in=None, 
    **kwargs):
    """
    Check if the token is valid

    Args:
        request (Request): The request
        res (Response): The response
        _in (Interface): The interface
        **kwargs: The keyword arguments
    """
    
    return res.success()