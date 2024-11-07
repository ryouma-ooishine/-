from django.forms import ModelForm
from .models import Page
from django import forms

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

class SellForm(ModelForm):
    class Meta:
        model = Page
        fields = ["sell_price","sell_shares","sell_day","sell_reason"]
        widgets = {
            'sell_reason': forms.Textarea(attrs={
                'placeholder': '売却理由を入力してください...',
                'rows': 6,  
                'style': 'width: 100%;' 
            })
        }