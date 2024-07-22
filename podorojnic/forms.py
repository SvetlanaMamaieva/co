from django import forms

from .models import Direction, Entry, Country, Info

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


class CountryForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = ['text',]
        labels = {'text': ''}



class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['text',]
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols': 80})}
