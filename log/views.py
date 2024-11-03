from django.shortcuts import render,redirect # type: ignore
from django.views import View # type: ignore
from datetime import datetime
from zoneinfo import ZoneInfo
from .models import Page
from .forms import PageForm
from django.views.generic import ListView

# Create your views here.
class IndexView(View):
    def get(self, request):
        datetime_now = datetime.now(
            ZoneInfo("Asia/Tokyo")
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
        # Pageオブジェクトを取得
        queryset = super().get_queryset()
        for page in queryset:
            page.total_amount = page.buy_price * page.buy_shares  # 総額を計算
        return queryset

    def get_context_data(self, **kwargs):
        # コンテキストに追加データを追加
        context = super().get_context_data(**kwargs)
        context['page_list'] = self.get_queryset()  # 計算されたオブジェクトのリストを渡す
        return context


index = IndexView.as_view()
page_create = PageCreateView.as_view()
page_list = PageListView.as_view()