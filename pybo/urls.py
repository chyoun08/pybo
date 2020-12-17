#--------------- [edit] ---------------#

from django.urls import path

from .views import base_views, question_views, answer_views, comment_views, vote_views

#app_name의 사용으로 좀더 세분화된 name들을 이용 가능하다.
app_name = 'pybo'

urlpatterns = [
    #url이 언제 순서가 question/id or id/question or question/get이렇게 바뀔지 모름으로 별칭사용이 코드 최적화에 좋다.
    #그때 사용하는것이 name이란 곳이다. name이란 고유값을 사용하여 url수정시에도 변동사항을 최소화할 수 있다.

    #base_views.py
    path('', base_views.index, name='index'),
    path('detail/<int:question_id>/', base_views.detail, name='detail'),

    #question_views.py
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),

    #answer_views.py
    path('answer/create/<int:question_id>/',answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
    
    #comment_views.py by question
    path('comment/create/question/<int:question_id>/', comment_views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', comment_views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', comment_views.comment_delete_question, name='comment_delete_question'),

    #comment_views.py by answer
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer, name='comment_delete_answer'),

     # vote_views.py
    path('vote/question/<int:question_id>/', vote_views.vote_question, name='vote_question'),
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer, name='vote_answer'),
    
]

#--------------- [edit] ---------------#