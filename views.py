
from kernel.http import Response
from .libs import create_token as create_token_lib

def create_token(request):
    """
        @description: 
    """
    res = Response()
    print (request.POST)
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