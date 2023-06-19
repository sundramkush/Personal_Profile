from django import forms
from .models import profile


class profilesform(forms.ModelForm):

    class Meta:
        model = profile
        fields = ('name','past_address','current_address','ph_number','user_id')

    def __init__(self, *args, **kwargs):
        super(profilesform,self).__init__(*args, **kwargs)
        self.fields['past_address'].required = False
        self.fields['user_id'].widget = forms.HiddenInput()
        