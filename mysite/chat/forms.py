from .models import UserAccount, User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class UserPageForm(ModelForm):
    class Meta:
        model = UserAccount
        fields = ('user_photo',)
