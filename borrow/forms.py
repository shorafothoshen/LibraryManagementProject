from django import forms
from .models import ReviewModel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ReviewForm(forms.ModelForm):
    body = forms.CharField(label="Review", widget=forms.Textarea)
    class Meta:
        model=ReviewModel
        fields=["body"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit_review', 'Send'))