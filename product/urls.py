from django.urls import path
from .views import *

urlpatterns = [
    path('books/', BookListView.as_view()),
    path('books/<int:pk>', BookDetailView.as_view()),
    path('author/', AuthorListView.as_view()),
    path('author/<int:pk>', AuthorDetailView.as_view()),
]