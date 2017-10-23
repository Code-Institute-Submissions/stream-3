from django import forms

from .models import Entertainer

class EntertainerForm(forms.ModelForm):

    class Meta:
        model = Entertainer
        fields = ('name', 'email', 'number', 'bio', 'location', 'entertainer_type', 'facebook', 'twitter', 'image', )