from django.urls import path

from . import views

app_name = 'sample'
urlpatterns = [
    path('booklist/', views.BookList.as_view(), name='booklist'),
    path('booklist_ajax/', views.BookJsonView.as_view(), name='booklist_ajax'),
    path('bookdetail/<int:pk>', views.BookDetail.as_view(), name='bookdetail'),
]