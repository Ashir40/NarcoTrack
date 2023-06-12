from django import forms
from .models import Center
from ckeditor.fields import RichTextField

class CenterForm(forms.ModelForm):
    description = RichTextField()

    class Meta:
        model = Center
        # fields = ('orgranization_name', 'mode_of_organization', 'image', 'description',)  # or specify the fields you want to include
        fields = '__all__' # or specify the fields you want to include

