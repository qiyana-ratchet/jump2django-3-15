from django.urls import path

from . import views
from .views import base_views, question_views, answer_views, profile_views

app_name = 'pybo'

urlpatterns = [
    # base
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),

    # question
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'),

    # answer
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),

    # ###############################################################################
    path('question/<int:question_id>/comment/', question_views.add_comment_to_question, name='add_comment_to_question'),
    path('answer/<int:answer_id>/comment/', answer_views.add_comment_to_answer, name='add_comment_to_answer'),

    path('category/<int:category_id>/', base_views.category_detail, name='category_detail'),

    path('profile/', profile_views.profile, name='profile'),
    path('recent-answers/', profile_views.recent_answers, name='recent_answers'),
    path('recent-comments/', profile_views.recent_comments, name='recent_comments'),
]
