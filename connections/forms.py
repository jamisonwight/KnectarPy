from django.forms import ModelForm
from .models import ConnectionInvite

class ConnectionForm(ModelForm):
    class Meta:
        # Note: must specify fields
        fields = '__all__'
        model = ConnectionInvite
        exclude = ['from_user', 'to_user']