from django.views import generic
from django.views.generic import DetailView, ListView
from django_datatables_view.base_datatable_view import BaseDatatableView

from .models import Book

class BookList(ListView):
    model = Book
    template_name = 'sample/book_list.html'

class BookJsonView(BaseDatatableView):
    # モデルの指定
    model = Book
    # 表示するフィールドの指定
    columns = ['id', 'title', 'author']

    def render_column(self, row, column):
        if column == 'id':
            return f'<a href="/sample/bookdetail/{row.id}">{row.id}</a>'
        else:
            return super(BookJsonView, self).render_column(row, column)

    # 検索方法の指定：部分一致
    def get_filter_method(self):
        return super().FILTER_ICONTAINS

class BookDetail(DetailView):
    model = Book
    template_name = 'sample/book_detail.html'