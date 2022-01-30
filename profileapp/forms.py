from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationFrom(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nicknames', 'message']
