from django.urls import path
from .views import BookListCreate, BookDetail, BookSearch, MemberListCreate, MemberDetail

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('books/search/', BookSearch.as_view(), name='book-search'),
    path('members/', MemberListCreate.as_view(), name='member-list-create'),
    path('members/<int:pk>/', MemberDetail.as_view(), name='member-detail'),
]
