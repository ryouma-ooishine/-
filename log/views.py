from django.shortcuts import render # type: ignore
from django.views import View # type: ignore
# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, "log/index.html")
    
index = IndexView.as_view()