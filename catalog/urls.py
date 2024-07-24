from django.urls import path

from catalog.views import (
    index,
)

urlpatterns = [
    path("", index, name="index"),
]

app_name = "catalog"
