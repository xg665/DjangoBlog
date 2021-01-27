from django.forms import ModelForm
from .models import Post
from django.utils.translation import ugettext_lazy as _

class BlogForm(ModelForm):

	class Meta:
		model = Post
		fields = ('title','problem_num','description','content','url')
		labels = {
            'content': _('Code'),
            'problem_num': _('Problem Number'),
        } 