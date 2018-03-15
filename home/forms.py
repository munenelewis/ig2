from django import forms
from home.models import Post,Image
from instapp.models import Profile


class Homeform(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'write a comment',
            'width': '560px',
            'border-bottom-color': 'white',
            'border-top-color': 'white',
        }
    ))

    class Meta:
        model = Post
        fields = (
            'post',
            )

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields=(
            "image",
            "image_name",
            "image_caption",
        )

        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=(
            "bio",
            "profile_img",
        )

        