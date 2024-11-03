from django.shortcuts import render,redirect # type: ignore
from django.views import View # type: ignore
from datetime import datetime
from zoneinfo import ZoneInfo
from .forms import PageForm

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


index = IndexView.as_view()
page_create = PageCreateView.as_view()