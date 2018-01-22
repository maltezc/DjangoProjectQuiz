from django.contrib.auth import get_user_model
#^returns user model that is currently active in this project
from django.contrib.auth.forms import UserCreationForm
#^money!!!

class UserCreateForm(UserCreationForm):
    #^make sure that class name is not same name as import
    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()
        #^when users sign up, this is what they will have access to


    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        #^if project was twitter,
        self.fields['email'].label = "Email Address"