from django.forms import ModelForm
from .models import Leveling


class LevelingForm(ModelForm):
    class Meta:
        model = Leveling
        fields = ['date', 'exp']
