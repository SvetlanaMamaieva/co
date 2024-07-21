from django import forms

from .models import Direction, Entry

class DirectionForm(forms.ModelForm):

    class Meta:
        model = Direction
        fields = ['text',]
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text',]
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols': 80})}


class SimpleForm(forms.Form):
    name = forms.CharField(max_length=100, label='Youe name')
    email = forms.EmailField(label='Your email')
