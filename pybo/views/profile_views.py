from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm

from django.contrib.auth import logout

from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from pybo.models import Question, Answer, Comment, Category
from pybo.forms import CommentForm

from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    user = request.user
    questions = Question.objects.filter(author=user)
    answers = Answer.objects.filter(author=user)
    comments = Comment.objects.filter(author=user)
    context = {
        'user': user,
        'questions': questions,
        'answers': answers,
        'comments': comments,
    }
    return render(request, 'pybo/profile.html', context)

#최근 10개 보여줌

def recent_answers(request):
    answers = Answer.objects.order_by('-create_date')[:10]
    context = {'answers': answers}
    return render(request, 'pybo/recent_answers.html', context)

def recent_comments(request):
    comments = Comment.objects.order_by('-create_date')[:10]
    context = {'comments': comments}
    return render(request, 'pybo/recent_comments.html', context)

