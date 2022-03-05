from django.urls import URLPattern


from django.urls import path
from agenda.views import index

urlpatterns = [
    path("", index)
]