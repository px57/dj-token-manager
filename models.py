
from django.forms.models import model_to_dict
from django.db import models
from django.utils import timezone
from django.urls import reverse

from gpm.models.base_metadata_model import BaseMetadataModel
from gpm.http import Response
from gpm.models.fetch_all_models_file import choicesListRelatedModels

from token_manager.rules.stack import TOKEN_MANAGER_RULESTACK


class TokenModels(BaseMetadataModel):
    """
        @description: 
    """
    token = models.CharField(
        max_length=255, 
        unique=True,
    )
    
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
        blank=True,
        choices=choicesListRelatedModels()
    )

    # -> Get the nice object
    relatedModelId = models.IntegerField(
        null=True,
        blank=True,
    )

    label = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        default=None,
        choices=TOKEN_MANAGER_RULESTACK.models_choices()
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
    
    def create_redirect_url(self, res: Response):
        """
            @description: 
            @param.res -> Response
        """
        path = reverse('token_manager__redirect')
        path = path.replace(':token', self.token)
        return res.create_client_url(path)
    
    def has_expired(self, _in) -> bool:
        """
            @description: 
        """

        # [interface.params]
        token_expiration_allow = _in.token_expiration_allow
        expiration_after = _in.expiration_after

        if not token_expiration_allow:
            return False
        
        now = timezone.now()
        if self.created_on + expiration_after < now:
            return True
        return False