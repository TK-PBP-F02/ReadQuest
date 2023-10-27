from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Forum, Replies
from books.models import Book
from users.models import User
from .forms import CreateForum, CreateReplies

def show_all_forum(request):
    forums = Forum.objects.all()
    return render(request, 'your_template.html', {'forums':forums})

def show_forum_per_book(request, idBook):
    book = get_object_or_404(Book, id=idBook)
    forums = Forum.objects.filter(book_section=book)
    return render(request, 'your_template.html', {'forums':forums})

def forum_detail(request, id):
    forum = get_object_or_404(Forum, id=id)
    replies = Replies.objects.filter(parent_forum=forum)
    return render(request, 'your_template.html', {'forums':forum,'replies':replies})

def add_forum(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = CreateForum()

    if request.method == 'POST':
        form = CreateForum(request.POST)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.book_section = book
            forum.author = request.user
            forum.save()
            return redirect('view-forum', book_id=book.id)

    return render(request, 'forum/add_forum.html', {'forum':form})

def reply(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    form = CreateReplies()
    
    if request.method == 'POST':
        form = CreateReplies(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.parent_forum = forum
            reply.author = request.user
            reply.save()
            return redirect('view-forum', book_id=forum.book_section.id)

    context = {
        'forum': forum,
        'form': form,
    }

    return render(request, 'forum/respond_forum.html', context)

@login_required
def delete_forum(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    
    if request.user == forum.author:
        forum.delete()
        return redirect('view-forum', book_id=forum.book_section.id)
    else:
        print()

@login_required    
def delete_reply(request, reply_id):
    reply = get_object_or_404(Replies, id=reply_id)
    
    if request.user == reply.author:
        reply.delete()
        return redirect('view-forum', book_id=reply.parent_forum.book_section.id)
    else:
        print()