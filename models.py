from django.db import models
from kernel.models.base_metadata_model import BaseMetadataModel
from django.forms.models import model_to_dict

class TokenModels(BaseMetadataModel):
    """
        @description: 
    """
    token = models.CharField(max_length=255, unique=True)
    profile = models.ForeignKey(
        'profiles.Profile', 
        on_delete=models.CASCADE, 
        related_name='token_profile',
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(default=True)

    number_of_uses = models.IntegerField(default=0)

    # -> Get the model object
    relatedModel = models.CharField(
        max_length=255, 
        null=True, 
        blank=True
    )

    # -> Get the nice object
    relatedModelId = models.IntegerField(
        null=True, 
        blank=True
    )

    class Meta:
        db_table = 'token'
        verbose_name = 'Token'
        verbose_name_plural = 'Tokens'

    def __str__(self):
        return self.token
    
    def serialize(self, request):
        """
            @description:
        """
        serialized = model_to_dict(self)
        if self.profile:
            serialized['profile'] = self.profile.serialize(request)
        return serialized