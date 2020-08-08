from django import forms
from android.models import allview

class DocumentForm(forms.ModelForm):
    class Meta:
        model = allview
        fields = ('gameimg', 'title','desc' )
