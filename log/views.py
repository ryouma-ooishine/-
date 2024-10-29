from django.shortcuts import render # type: ignore
from django.views import View # type: ignore
from datetime import datetime
from zoneinfo import ZoneInfo


# Create your views here.
class IndexView(View):
    def get(self, request):
        datetime_now = datetime.now(
            ZoneInfo("Asia/Tokyo")
        ).strftime("%Y年%月%d日 %H:%M:%S")
        return render(
            request, "log/index.html",{"datetime_now":datetime_now})
index = IndexView.as_view()