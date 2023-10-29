from django.forms import ModelForm, ModelChoiceField
from round_table.models import Forum, Replies
from books.models import Book
 
class CreateForum(ModelForm):
    def __init__(self, *args, **kwargs):
        book_id = kwargs.pop("book_id", None)
        super(CreateForum, self).__init__(*args, **kwargs)
        if book_id is not None:
            self.fields["book"].initial = book_id

    book = ModelChoiceField(
        queryset=Book.objects.all(),
        empty_label="Select a book",
    )
    class Meta:
        model = Forum
        fields = ["book", "title", "content"]
 
class CreateReplies(ModelForm):
    class Meta:
        model = Replies
        fields = ["content"]