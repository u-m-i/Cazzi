
from django import forms

class ProfileForm(forms.Form):
    """ All the profile fields
    """
    website = forms.URLField()
    biography = forms.Textarea()
    phone_number = forms.CharField()
    picture = forms.ImageField()