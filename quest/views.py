from django.shortcuts import get_object_or_404, render
from books.models import Book
from .models import Quest, QuestContainer
# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from .forms import QuestForm  # Import your QuestForm
from django.views.decorators.csrf import csrf_exempt
from users.models import User
from django.db.models import F
from django.core import serializers



def roler(request):
    user = request.user
    role = 'none'
    if user.is_anonymous:
        return role
    if user.role == "PENGGUNA":
        role = 'pengguna'
    elif user.role == "ADMIN":
        role = 'admin'
    return role

@csrf_exempt
def create_quest(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        desc = request.POST.get("desc")
        point = request.POST.get("point")
        goal = request.POST.get("goal")
        type = request.POST.get("quest_type")
        id = int(request.POST.get("book_id"))
        amount = int(request.POST.get("amount"))
        if id == 0:
            Quest.objects.create(name=name, desc=desc, goal=goal, point=point, type=type, amount=amount, container=None)
        elif amount == 0:
            book = Book.objects.get(pk=id)
            container, created = QuestContainer.objects.get_or_create(book_key=book)
            Quest.objects.create(name=name, desc=desc, goal=goal, point=point, type=type, container=container)
            book.quest_amount = 1
            book.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def quest_book_detail(request, pk):
    user = request.user
    book = get_object_or_404(Book, pk=pk)
    container = QuestContainer.objects.filter(book_key = book)
    return render(request, 'quest_book_detail.html', {'book': book, 'container':container, 'role':roler(request), 'user':user})

@csrf_exempt
def delete_quest(request):
    if request.method == "POST":
        try:
            id = int(request.POST.get("book_id"))
            quest = Quest.objects.get(pk=id)
            quest.delete()
            return HttpResponse(b"DELETED", status=201)
        except:
            return HttpResponseNotFound()
            # return render(request, 'pagenotfound.html', status=404)

    return HttpResponseNotFound()

def create_quest_view(request):
    if request.method == 'POST':
        form = QuestForm(request.POST)
        if form.is_valid():
            quest = form.save()
            # You can customize the response data as needed
            return JsonResponse({'success': 'Quest created successfully'})
        else:
            # Handle form validation errors
            return JsonResponse({'errors': form.errors}, status=400)  # Status 400 for bad request

def quest_detail(request, id):
    quest = Quest.objects.get(pk=id)
    user = request.user
    return render(request, 'quest_detail.html', {'quest': quest, 'user':user, 'role':roler(request)})

def view_quest(request):
    user = request.user
    books = Book.objects.all()
    quests = Quest.objects.all()
    if user.is_anonymous:
        user = "none"
        return render(request, 'quest.html', {'books': books, 'user':user, 'role':'not login', 'quests':quests})
    if user.role == "PENGGUNA":
        username = user.username
        point = user.point
        return render(request, 'quest.html', {'books': books, 'user':user, 'username':username, 'point':point, 'role':'pengguna', 'quests':quests})
    elif user.role == "ADMIN" :
        username = user.username
        return render(request, 'quest.html', {'books': books, 'user':user, 'username':username, 'role':'admin', 'quests':quests})

def quest_point(request):
    user = request.user
    point = 0
    quests = Quest.objects.all()

    for quest in quests:
        if quest.goal == 'Readded' and user.readed >= quest.amount:
            point += quest.point
        elif quest.goal == 'Buyed' and user.buyed >= quest.amount:
            point += quest.point
        elif quest.goal == 'Review' and user.reviewed >= quest.amount:
            point += quest.point

    # Update the user's point field in the database
    User.objects.filter(pk=user.pk).update(point=point)

    # Fetch the user object again to get the updated value
    user = User.objects.get(pk=user.pk)
            