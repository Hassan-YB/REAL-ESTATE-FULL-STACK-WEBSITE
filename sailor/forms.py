from django import forms 
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Submitpropertyform(forms.ModelForm):

    class Meta:
        model = Advertisement
        fields = ("type","price","id","title","listing_type","bedrooms","bathrooms","floor_number","neigborhood","description","built_up_year","ad_price_type","expiry","area","country","state","city","street_and_house_no","owner")

class Newsletterform(forms.ModelForm):
    
    class Meta:
        model = Newsletter
        fields = ("email",)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
       