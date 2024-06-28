from django import forms

from v_app.models import Category, Author


class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class AddCatForm(forms.Form):
    name = forms.CharField(label='name', widget=forms.TextInput())


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class AddAuthorForm(forms.Form):
    name = forms.CharField(label='name', widget=forms.TextInput())