from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count
from .models import Book
from .forms import BookForm


def book_list(request):
    query = request.GET.get('q')

    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query)
        )
    else:
        books = Book.objects.all()

    recommended_author = (
        Book.objects.values('author')
        .annotate(total=Count('author'))
        .order_by('-total')
        .first()
    )

    return render(request, 'books/book_list.html', {
        'books': books,
        'recommended_author': recommended_author,
    })


def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'books/book_form.html', {'form': form})


def book_update(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'books/book_form.html', {'form': form})


def book_delete(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.delete()
        return redirect('book_list')

    return render(request, 'books/book_delete.html', {'book': book})
