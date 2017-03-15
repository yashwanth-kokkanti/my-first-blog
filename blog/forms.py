from django import forms

from . models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image']
        labels = {
             'image': 'Upload Pic',}
		
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text', )
		
class RegistrationForm(forms.Form):
    username = forms.CharField(label="UserName", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}), required=True,)
    
    email = forms.EmailField(label="Email", max_length=100, widget=forms.TextInput(attrs={'autocorrect':'off','autocapitalize':'none','class':'form-control','placeholder':'Enter Email'}), required=True,)
    
    password1 = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput(attrs={'type':'password','class':'form-control','placeholder':'Enter Password'}),required=True, )
    
    password2 = forms.CharField(label="Password Again", widget=forms.PasswordInput(attrs={'type':'password','class':'form-control','placeholder':'Enter Password Again'}),required=True,)

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError("Passwords Do Not Match")