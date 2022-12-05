from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Book
from django.contrib.auth.decorators import login_required
from .forms import FinishBookForm, BookForm, StartBookForm
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(request):
    template = loader.get_template('booksapp/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


@login_required
def home(request):
    user = request.user
    total_book_count = Book.objects.filter(user=user).count() if user.is_authenticated else Book.objects.all().count()
    not_started_book_count = Book.objects.filter(user=user).filter(read_status="NOT_STARTED").count()
    in_progress_book_count = Book.objects.filter(user=user).filter(read_status="IN_PROGRESS").count()
    finished_book_count = Book.objects.filter(user=user).filter(read_status="FINISHED").count()
    books = Book.objects.filter(user=user)
    recent_books = Book.objects.filter(user=user).order_by('-id')[:5]
    template = loader.get_template('booksapp/home.html')
    context = {
        'total_book_count': total_book_count,
        'not_started_book_count': not_started_book_count,
        'in_progress_book_count': in_progress_book_count,
        'finished_book_count': finished_book_count,
        'books': books,
        'recent_books': recent_books
    }
    return HttpResponse(template.render(context, request))


@login_required
def book_list(request):
    user = request.user
    book_object = Book.objects.filter(user=user) if user.is_authenticated else Book.objects.all()
    book_title = request.GET.get('book_title')
    if book_title != '' and book_title is not None:
        book_object = book_object.filter(title__icontains=book_title)
    paginator = Paginator(book_object, 10)
    page = request.GET.get('page')
    book_object = paginator.get_page(page)
    context = {
        'book_object': book_object,
        'user': user,
    }
    return render(request, 'booksapp/booklist.html', context)


@login_required
def reading_list(request):
    user = request.user
    book_object = Book.objects.filter(user=user) if user.is_authenticated else Book.objects.all()
    not_started_book = Book.objects.filter(user=user).filter(read_status="NOT_STARTED")
    book_title = request.GET.get('book_title')
    if book_title != '' and book_title is not None:
        book_object = book_object.filter(title__icontains=book_title)
        not_started_book = not_started_book.filter(title__icontains=book_title)
    paginator = Paginator(not_started_book, 10)
    page = request.GET.get('page')
    not_started_book = paginator.get_page(page)
    context = {
        'book_object': book_object,
        'user': user,
        'not_started_book': not_started_book
    }
    return render(request, 'booksapp/reading-list.html', context)


@login_required
def currently_reading(request):
    user = request.user
    book_object = Book.objects.filter(user=user) if user.is_authenticated else Book.objects.all()
    in_progress_book = Book.objects.filter(user=user).filter(read_status="IN_PROGRESS")
    book_title = request.GET.get('book_title')
    if book_title != '' and book_title is not None:
        book_object = book_object.filter(title__icontains=book_title)
        in_progress_book = in_progress_book.filter(title__icontains=book_title)
    paginator = Paginator(in_progress_book, 10)
    page = request.GET.get('page')
    in_progress_book = paginator.get_page(page)
    context = {
        'book_object': book_object,
        'user': user,
        'in_progress_book': in_progress_book,
    }
    return render(request, 'booksapp/currently-reading.html', context)


@login_required
def finished_books(request):
    user = request.user
    book_object = Book.objects.filter(user=user) if user.is_authenticated else Book.objects.all()
    finished_book = Book.objects.filter(user=user).filter(read_status="FINISHED")
    book_title = request.GET.get('book_title')
    if book_title != '' and book_title is not None:
        book_object = book_object.filter(title__icontains=book_title)
        finished_book = finished_book.filter(title__icontains=book_title)
    paginator = Paginator(finished_book, 10)
    page = request.GET.get('page')
    finished_book = paginator.get_page(page)
    context = {
        'book_object': book_object,
        'user': user,
        'finished_book': finished_book
    }
    return render(request, 'booksapp/finished-books.html', context)


@login_required
def detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {
        'book': book
    }
    return render(request, 'booksapp/detail.html', context)


@login_required
def create_book(request):
    form = BookForm(request.POST or None, request.FILES or None)
    user = request.user

    if form.is_valid():
        form.save()
        messages.success(request, f'This book has been added')
        return redirect('/booksapp/booklist')

    return render(request, 'booksapp/book-form.html', {'form': form, 'user': user})


@login_required
def update_book(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, request.FILES or None, instance=book)

    if form.is_valid():
        form.save()
        messages.success(request, f'This book has been updated')
        return redirect('/booksapp/booklist')

    return render(request, 'booksapp/book-form.html', {'form': form})


@login_required
def delete_book(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        book.delete()
        messages.success(request, f'This book has been deleted')
        return redirect('/booksapp/booklist')

    return render(request, 'booksapp/book-delete.html', {'book': book})


@login_required
def start_book(request, id):
    book = Book.objects.get(id=id)
    form = StartBookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        messages.success(request, f"This book is now marked as being currently read")
        return redirect('/booksapp/currently-reading')

    return render(request, 'booksapp/start-form.html', {'form': form, 'book': book})


@login_required
def finish_book(request, id):
    book = Book.objects.get(id=id)
    form = FinishBookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        messages.success(request, f"This book is now marked as finished")
        return redirect('/booksapp/finished-books')

    return render(request, 'booksapp/finish-form.html', {'form': form, 'book': book})
