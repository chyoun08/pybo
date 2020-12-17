# ---------------------------------------- [edit] ---------------------------------------- #
from django import forms
from .models import Question, Answer, Comment


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']

        labels = {
            'subject': '제목',
            'content': '내용',
        }
        """
        class에서도 가능하고 html내부에서도 조정이 가능하다.
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }

        """
# ---------------------------------------------------------------------------------------- #

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

# ---------------------------------------------------------------------------------------- #

# ---------------------------------------- [edit] ---------------------------------------- #
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }
# ---------------------------------------------------------------------------------------- #