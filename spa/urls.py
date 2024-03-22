from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("section/<int:page>", views.section, name="section"),
]
