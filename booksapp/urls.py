from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('booklist/', views.book_list, name="book_list"),
    path('reading-list/', views.reading_list, name="reading_list"),
    path('currently-reading/', views.currently_reading, name="currently_reading"),
    path('finished-books/', views.finished_books, name="finished_books"),
    path('add-book/', views.create_book, name="create_book"),
    path('update-book/<int:id>', views.update_book, name="update_book"),
    path('delete-book/<int:id>', views.delete_book, name="delete_book"),
    path('start-book/<int:id>', views.start_book, name="start_book"),
    path('finish-book/<int:id>', views.finish_book, name="finish_book"),
    path('book/<int:book_id>', views.detail, name="detail"),
]
