from django.forms import ModelForm, ModelChoiceField
from round_table.models import Forum, Replies
from books.models import Book
 
class CreateForum(ModelForm):
    class Meta:
        model = Forum
        fields = ["book", "title", "content"]
 
class CreateReplies(ModelForm):
    class Meta:
        model = Replies
        fields = ["content"]