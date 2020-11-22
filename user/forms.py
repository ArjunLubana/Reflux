from django import forms
from django.forms.utils import ErrorList

class MessageForm(forms.Form):
	name = forms.CharField(max_length=100)
	email = forms.EmailField()
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)


'''
This class is used to edit the HTML element enclosing an error message during form instantiation


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<div class="error">%s</div>' % e for e in self])*/'''