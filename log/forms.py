from django.forms import ModelForm
from .models import Page

class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ['company_name', 'buy_day', 'buy_price', 'buy_shares']