from django import forms

class UploadFileForm(forms.Form):
    csv_file = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))

class DataEntryForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Write  name here'
            }
        )
        )
    address  = forms.CharField(widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Write  address here'
            }
        ))