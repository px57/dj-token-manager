
from django.shortcuts import render
from kernel.http import Response 
from .libs import create_token as create_token_lib
from .libs import find_token as find_token_lib
from .libs import use_token as use_token_lib

def create_token(request):
    """
        @description: 
    """
    res = Response(request=request)
    max_size = request.POST.get('max_size', 32)
    relatedModel = request.POST.get('relatedModel')
    relatedModelId = int(request.POST.get('relatedModelId'))

    dbToken = create_token_lib(
        max_size=max_size, 
        relatedModel=relatedModel, 
        relatedModelId=relatedModelId
    )
    res.token = dbToken.serialize(request)
    return res.success()

def token_exists(request):
    """
        @description: Verify if the token exists. 
    """
    res = Response(request=request)
    
    return res.success()

def use_token(request):
    """
        @description: Use the token and delete it from the database
    """
    res = Response(request=request)
    return res.success()

def create_token(request):
    """
        @description: Create a token
    """
    res = Response(request=request)
    return res.success()
