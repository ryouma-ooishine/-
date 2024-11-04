from django.forms import ModelForm
from .models import Page
from django import forms
from .models import Log

class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ['company_name', 'buy_day', 'buy_price', 'buy_shares','buy_reason']
        widgets = {
            'buy_reason': forms.Textarea(attrs={
                'placeholder': '購入理由を入力してください...',
                'rows': 6,  
                'style': 'width: 100%;' 
            })
        }

