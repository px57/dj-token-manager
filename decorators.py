
from kernel.http import Response
from .libs import create_token as create_token_lib
from .libs import find_token as find_token_lib
from .libs import use_token as use_token_lib

def load_token(function):
    """
        @description: Load the token from the request.
        @params.function: The function that will be called after the token is loaded.   
        @params.required: If the token is required or not.
        @params.use_token: If the token must be used or not.
        @return: The function that will be called after the token is loaded.
    """
    def wrap(request, *args, **kwargs):
        token = request.POST.get('token', request.GET.get('token', None))
        request.token = find_token_lib(token=token)
        return function(request, *args, **kwargs)
    
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def token_required(function):
    """
        @description: Token required decorator
        @params.function: The function that will be called after the token is loaded.   
    """
    def wrap(request, *args, **kwargs):
        if request.token is None:
            return Response(request=request).error(
                message='Token is required'
            )
        return function(request, *args, **kwargs)
    
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
