from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from round_table.models import Forum, Replies
from users.models import User
from django.http import HttpResponse, HttpResponseNotFound
from .forms import CreateForum, CreateReplies

def roler(user):
    role = 'none'
    if user.role == "PENGGUNA":
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
    return render(request, 'forum_detail.html', {'forum':forum,'replies':replies,'role':roler(request.user)})

def add_forum(request):
    form = CreateForum(request.POST or None)

    if request.user.is_anonymous:
        return redirect('user:login')
    elif form.is_valid() and request.method == 'POST':
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
        results = title_results.union(content_results)
    else:
        results = None
    return render(request, 'search_forums.html', {'results': results,'q':query,'username':request.user.username,'role':roler(request.user)})
