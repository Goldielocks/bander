from django import forms
from django.contrib.auth.models import User
from BandList.models import User, UserProfile

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('shows', 'bands', 'location', 'max_distance')
