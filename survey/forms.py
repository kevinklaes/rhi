from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class FormHorizontalForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super(FormHorizontalForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'

class FormHorizontalModelForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(FormHorizontalModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'

class PageOne(FormHorizontalForm):
    
