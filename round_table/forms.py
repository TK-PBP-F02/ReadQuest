from django.forms import ModelForm
from round_table.models import Forum, Replies
 
class CreateForum(ModelForm):
    class Meta:
        model = Forum
        fields = ["title", "content"]
 
class CreateReplies(ModelForm):
    class Meta:
        model = Replies
        fields = ["content"]