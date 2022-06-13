from django.forms import ModelForm
from .models import GameetUser
from django.contrib.auth.models import User


#Create a User form
class GameetUserForm(ModelForm):

    class Meta:
        model = GameetUser
        fields = (
            'telephone', 'picture'
        )  #If we want all parameters we can just use fields = "_all_"


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
