from django.db import models

from django.contrib.auth.models import User
#--------------- [edit] ---------------#

class Question(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')

    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    #null값이 들어가도 괜찮다는 의미이다 null=true 및 blank=true
    modify_date = models.DateTimeField(null=True, blank=True)

    #author와 마찬가지로 User란 객체를 같이 공유하고 있음으로 구분을 주기위한 이름 설정이 반드시 필요하다.
    voter = models.ManyToManyField(User, related_name='voter_question')

    def __str__(self):
        return self.subject

class Answer(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    modify_date = models.DateTimeField(null=True, blank=True)
    #Question와 마찬가지로 realtedname을 지정해주어야한다.
    voter = models.ManyToManyField(User, related_name='voter_amswer')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
    
#--------------- [edit] ---------------#