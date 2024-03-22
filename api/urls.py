from django.urls import path
from .views import *

urlpatterns = [
    path('',getRoutes,name="routes"),
    path('notes/',getNotes,name="notes"),
    path('notes/create/',addNotes,name="add-notes"),
    path('notes/<int:pk>/',getNote,name="note"),
    path('notes/<int:pk>/update/',updateNote,name="update-note"),
    path('notes/<int:pk>/delete/',deleteNote,name="delete-note"),
]