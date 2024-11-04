from django.urls import path # type: ignore
from . import views

app_name = "log"
urlpatterns=[
    path("",views.index,name ="index"),
    path("page/create/",views.page_create,name="page_create"),
    path("page/list/",views.page_list,name="page_list"),
    path("page/update/<uuid:pk>/",views.page_update,name="page_update"),
]