from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class ExampleForm(forms.Form):
    Date_From = forms.DateField(widget=DateInput)
    Date_To = forms.DateField(widget=DateInput)