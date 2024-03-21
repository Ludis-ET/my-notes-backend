from django.urls import path
from .views import *

urlpatterns = [
    path('',getRoutes,name="routes"),
    path('notes/',getNotes,name="notes"),
    path('notes/<int:pk>/',getNote,name="note"),
    path('notes/<int:pk>/update/',updateNote,name="update-note"),
]