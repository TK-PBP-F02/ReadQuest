import json
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from books.models import Book
from round_table.models import Forum, Replies
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from .forms import CreateForum, CreateReplies
from django.db.models import Q

def roler(user):
    if user.is_anonymous:
        role = 'none'
    elif user.role == "PENGGUNA":
        role = 'pengguna'
    elif user.role == "ADMIN":
        role = 'admin'
    return role

def show_all_forum(request):
    forums = Forum.objects.all()
    return render(request, 'forum.html', {'forums':forums,'role':roler(request.user)})

def forum_detail(request, id):
    forum = get_object_or_404(Forum, id=id)
    replies = Replies.objects.filter(parent_forum=forum)
    book = forum.book
    return render(request, 'forum_detail.html', {'forum':forum,'replies':replies,'role':roler(request.user), 'book':book})

def add_forum(request, book_id=None):
    form = CreateForum(book_id=book_id)

    if request.user.is_anonymous:
        return redirect('user:login')
    elif request.method == 'POST':
        form = CreateForum(request.POST, book_id=book_id)
        if form.is_valid():
    
            forum = form.save(commit=False)
            forum.author = request.user
            forum.save()
            return redirect('round_table:show_all_forum')

    return render(request, 'add_forum.html', {'form':form,'role':roler(request.user)})

def add_reply(request, id):
    forum = get_object_or_404(Forum, id=id)
    form = CreateReplies(request.POST or None)
    
    if request.user.is_anonymous:
        return redirect('user:login')
    elif form.is_valid() and request.method == 'POST':
        reply = form.save(commit=False)
        reply.parent_forum = forum
        reply.author = request.user
        reply.save()
        return redirect('round_table:forum_detail', id=id)

    return render(request, 'add_reply.html', {'forum':forum,'form':form,'role':roler(request.user)})

def delete_forum(request, id):
    forum = get_object_or_404(Forum, id=id)
    
    if request.user == forum.author:
        forum.delete()
        return redirect('round_table:show_all_forum')
    
    return redirect('round_table:forum_detail', id=id)
  
def delete_reply(request, id):
    reply = get_object_or_404(Replies, id=id)
    
    if request.user == reply.author:
        reply.delete()
        return redirect('round_table:forum_detail', id=id)
    
    return redirect('round_table:forum_detail', id=id)

def search_forums(request):
    if 'q' in request.GET:
        query = request.GET['q']
        title_results = Forum.objects.filter(title__icontains=query)
        content_results = Forum.objects.filter(content__icontains=query)
        book_results = Forum.objects.filter(
            Q(book__title__icontains=query) | Q(book__author__icontains=query)
        )
        results = title_results.union(content_results)
        results = results.union(book_results)
    else:
        results = None
    return render(request, 'search_forums.html', {'results': results,'q':query,'username':request.user.username,'role':roler(request.user)})

def get_forums_json(request):
    forums = Forum.objects.all()
    forum_data = []

    for forum in forums:
        data = {
            "id": forum.id,
            "book_title": forum.book.title,
            "book_author": forum.book.author,
            "book_thumbnail": forum.book.image_url,
            "title": forum.title,
            "content": forum.content,
            "author": forum.author.username,
            "created_at": forum.created_at,
            "is_owner": request.user.is_authenticated and request.user == forum.author,
        }
        forum_data.append(data)

    return JsonResponse(forum_data, safe=False)

@csrf_exempt
def delete_forum_ajax(request, id):
    if request.method == 'DELETE':
        item = get_object_or_404(Forum, id=id)
        item.delete()
        return HttpResponse(b"DELETED", status=200)
    
    return HttpResponseNotFound()

def get_replies_json(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    replies = Replies.objects.filter(parent_forum=forum)
    forum_data = []

    for reply in replies:
        data = {
            "id": reply.id,
            "ForumId": forum_id,
            "content": reply.content,
            "author": reply.author.username,
            "created_at": reply.created_at,
            "is_owner": request.user.is_authenticated and request.user == reply.author,
        }
        forum_data.append(data)

    return JsonResponse(forum_data, safe=False)

@csrf_exempt
def delete_reply_ajax(request, forum_id, reply_id):
    if request.method == 'DELETE':
        item = get_object_or_404(Replies, id=reply_id)
        item.delete()
        return HttpResponse(b"DELETED", status=200)
    
    return HttpResponseNotFound()

@csrf_exempt
def create_forum_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        book_from_id = get_object_or_404(Book, pk=int(data['book']))

        new_forum = Forum.objects.create(
            author = request.user,
            book = book_from_id,
            title = data["title"],
            content = data["content"],
        )
        new_forum.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt
def create_replies_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        parent_forum_from_id = get_object_or_404(Forum, pk=int(data['parent_forum']))

        new_replies = Replies.objects.create(
            author = request.user,
            parent_forum = parent_forum_from_id,
            content = data["content"],
        )

        new_replies.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt
def delete_forum_flutter(request, id):
    if request.method == 'DELETE':
        forum = get_object_or_404(Forum, pk=id)
        forum.delete()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
