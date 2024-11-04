from django.shortcuts import render,redirect ,get_object_or_404
from django.views import View 
from datetime import datetime
import pytz
from .models import Page, Log
from .forms import PageForm
from django.views.generic import ListView,UpdateView
from django.urls import reverse  # reverseをインポート

class IndexView(View):
    def get(self, request):
        datetime_now = datetime.now(
            pytz.timezone("Asia/Tokyo")
        ).strftime("%Y年%月%d日 %H:%M:%S")
        return render(
            request, "log/index.html",{"datetime_now":datetime_now})

class PageCreateView(View):
    def get(self,request):
        form = PageForm()
        return render(request, "log/page_form.html",{"form":form})
    
    def post(self, request, *args, **kwargs):
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("log:index")
        return render(request, "log/page_form.html",{"form":form})
    
class PageListView(ListView):
    model = Page
    def get_queryset(self):
        queryset = super().get_queryset()
        for page in queryset:
            page.total_amount = page.buy_price * page.buy_shares 
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_list'] = self.get_queryset()
        return context



class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name = "log/update.html"

    def get_success_url(self):
        return reverse("log:page_list") 

index = IndexView.as_view()
page_create = PageCreateView.as_view()
page_list = PageListView.as_view()
page_update = PageUpdateView.as_view()