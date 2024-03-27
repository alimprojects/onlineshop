from django import forms
from .models import *
 
 
# creating a form
class ReviewsForm(forms.ModelForm):
    class Meta: 
        model = Reviews
        fields = ['product_id', 'customer_name', 'customer_email', 'review', 'rate']
