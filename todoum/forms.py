from django import forms

from todoum.models import Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        exclude = ['region']
