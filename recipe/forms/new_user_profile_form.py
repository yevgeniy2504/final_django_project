from django import forms
from ..models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'photo', 'bio']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter author name', 'maxlength': '200'}),
        }
        labels = {
            'name': 'Author name',
            'photo': 'Author photo',
            'bio': 'Author bio',
        }
        help_texts = {
            'name': 'Введите имя пользователя',
            'photo': 'Загрузите фотографию пользователя',
            'bio': 'Личная информация о пользователе',
        }

    def clean_name(self):
        data = self.cleaned_data['name']
        if len(data) < 3:
            raise forms.ValidationError('Имя пользователя должно быть больше 3 символов')
        return data

    def clean_photo(self):
        data = self.cleaned_data['photo']
        if data:
            if len(data.name) > 100:
                raise forms.ValidationError('Имя файла фотографии не должно превышать 100 символов')
        return data
