
from kernel.http import Response
from .libs import create_token as create_token_lib
from .libs import find_token as find_token_lib
from .libs import use_token as use_token_lib

def load_token(function, required=True, use_token=False):
    """
        @description: Load the token from the request.
        @params.function: The function that will be called after the token is loaded.   
        @params.required: If the token is required or not.
        @params.use_token: If the token must be used or not.
        @return: The function that will be called after the token is loaded.
    """
    def wrap(request, *args, **kwargs):
        token = request.POST.get('token', request.GET.get('token', None))
        if token is None and required:
            return Response(request=request).error(
                message='Token is required'
            )
        elif token is None and not required:
            return function(request, *args, **kwargs)

        if use_token is False:
            request.token = find_token_lib(token=token)
        else:
            request.token = use_token_lib(token=token)
        return function(request, *args, **kwargs)
    
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


@load_token(required=True)
def token_required(function):
    """
        @description: Token required decorator
        @params.function: The function that will be called after the token is loaded.   
    """
    def wrap(request, *args, **kwargs):
        return function(request, *args, **kwargs)
    
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

@load_token(required=False)
def load_token_optional(function):
    """
        @description: Token optional decorator
        @params.function: The function that will be called after the token is loaded.   
    """
    def wrap(request, *args, **kwargs):
        return function(request, *args, **kwargs)
    
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap