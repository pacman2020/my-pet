from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = (
            'user_id','city','phone','email','description','photo',
            )
