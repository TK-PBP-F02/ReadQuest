from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.http import HttpResponseRedirect, JsonResponse
from make_journey_jurnal.forms import BookForm, BookDeleteForm
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def create_book(request):
    form = BookForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('make_journey_jurnal:display_all_books'))

    context = {'form': form}
    return render(request, "create_book.html", context)

def display_all_books(request):
    books = Book.objects.all()
    user = request.user
    if user.is_anonymous:
        user = "none"
        return render(request, 'book1.html', {'books': books, 'user':user, 'role':'not login'})
    elif user.role == "PENGGUNA":
        username = user.username
        point = user.point
        return render(request, 'book1.html', {'books': books, 'username':username, 'point':point, 'role':'pengguna'})
    elif user.role == "ADMIN" :
        username = user.username
        return render(request, 'book1.html', {'books': books, 'username':username, 'role':'admin'})
    return render(request, 'book1.html', {'books': books, 'username' : user.username, 'role':'none'})

def book_detail_make(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail_make.html', {'book': book})


def delete_book_make(request):
    if request.method == 'POST':
        form = BookDeleteForm(request.POST)
        if form.is_valid():
            book_id = form.cleaned_data['book_id']
            book = Book.objects.get(pk=book_id)
            book.delete()
            return HttpResponseRedirect(reverse('make_journey_jurnal:display_all_books'))  
    else:
        form = BookDeleteForm()
    return render(request, 'remove_book_make.html', {'form': form})

