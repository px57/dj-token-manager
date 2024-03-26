"""
Is used to validate the token, request from the user.
"""


from django import forms

class TokenValidator(forms.Field):
    """
        @description: Valider le pseudo de l'utilisateur
    """   
    default_validators = []

    def __init__(self, required=True):
        super().__init__()
        self.required = required

    def to_python(self, token):
        """
            @description:
        """
        return token