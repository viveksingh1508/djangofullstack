from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.notes, name="notes"),
    path("notes/<slug:slug>", views.note_details, name="note-details"),
]
