from django import forms
from .models import UserProfile, Neighborhood, Business, Post, Comment


class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput()

    class Meta:
        model = UserProfile
        fields = ('Profile_photo', 'first_name',
                  'last_name', 'bio', 'phone', 'email')


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user', 'neighborhood']


class PostForm(forms.ModelForm):
    CHOICES = (('1', 'Amber',), ('2', 'Normal',))
    type = forms.ChoiceField(widget=forms.Select, choices=CHOICES)

    class Meta:
        model = Post
        fields = ('title', 'content', 'type')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
