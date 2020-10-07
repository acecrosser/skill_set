from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
    # required=False - вкл необязательное поле


class CommentForm(forms.ModelForm):
    # для работы формы, надо указать просто какую модель использовать в подклассе Meta
    class Meta:
        model = Comment
        fields = ('name', 'body')  # поля которые хотим указывать при заполнениии (есть еще 'email')


