from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = (
            'user_id','city','phone','email','description','photo',
            )


# user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     city = models.CharField(max_length=100)
#     phone = models.CharField(max_length=11)
#     email = models.EmailField()
#     active = models.BooleanField(default=True)
#     description = models.TextField()
#     photo = models.ImageField(upload_to='media', null=True)