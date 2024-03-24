
from django import forms

from token_manager.libs import find_token as find_token_lib

class CheckIsValidForm(forms.Form):
    """
    CheckIsValidForm
    """

    def __init__(self, *args, **kwargs):
        super(CheckIsValidForm, self).__init__(*args, **kwargs)
        self.clean_token = clean_token.__get__(self)

    token = forms.CharField(
        required=True,
    )


def clean_token(self):
    """
    @description: 
    """
    token = self.cleaned_data.get('token')

    # [interface.params]
    token_max_size = self._in.token_max_size
    token_min_size = self._in.token_min_size
    token_character_list = self._in.token_character_list

    # Check if the token is too long
    if len(token) > token_max_size:
        raise forms.ValidationError(
            "Token is too long"
        )
    
    # Check if the token is too short
    if len(token) < token_min_size:
        raise forms.ValidationError(
            "Token is too short"
        )
    
    # Check if the token contains invalid characters
    for char in token:
        if char not in token_character_list:
            raise forms.ValidationError(
                "Token contains invalid characters:  " + char + " "
            )

    dbToken = find_token_lib(token)

    # Check if the token exists
    if dbToken is None:
        raise forms.ValidationError(
            "Token not found"
        )

    # Check if the token has expired
    if dbToken.has_expired(self._in):
        raise forms.ValidationError(
            "Token has expired"
        )
    
    # The interface corrensponding to the _in.label
    if dbToken.label != self._in.label:
        raise forms.ValidationError(
            "The interface does not correspond to the label"
        )
    return dbToken
