# base_views.py
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from pybo.models import Question, Category

def initialize_categories():
    if not Category.objects.exists():
        Category.objects.create(name='질의응답')
        Category.objects.create(name='자유게시판')

def index(request):
    initialize_categories()
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    question_list = Question.objects.order_by('-create_date')
    categories = Category.objects.all()  # 카테고리 목록
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목
            Q(content__icontains=kw) |  # 내용
            Q(answer__content__icontains=kw) |  # 답변 내용
            Q(author__username__icontains=kw) |  # 질문 글쓴이
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이
        ).distinct()
    paginator = Paginator(question_list, 5)  # 페이지당 5개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'categories': categories}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    initialize_categories()
    question = get_object_or_404(Question, pk=question_id)
    question.views += 1  # 조회 수 증가
    question.save()
    sort = request.GET.get('sort', 'recent')  # 기본 정렬은 'recent'로 설정

    if sort == 'recommend':
        answer_list = question.answer_set.annotate(num_votes=Count('voter')).order_by('-num_votes', '-create_date')
    else:  # 기본값은 'recent'
        answer_list = question.answer_set.annotate(num_votes=Count('voter')).order_by('-create_date')

    paginator = Paginator(answer_list, 3)  # 페이지당 3개의 답변
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'question': question, 'page_obj': page_obj, 'sort': sort}
    return render(request, 'pybo/question_detail.html', context)

def category_detail(request, category_id):
    initialize_categories()
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    category = get_object_or_404(Category, pk=category_id)
    question_list = category.questions.order_by('-create_date')
    categories = Category.objects.all()  # 카테고리 목록
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목
            Q(content__icontains=kw) |  # 내용
            Q(answer__content__icontains=kw) |  # 답변 내용
            Q(author__username__icontains=kw) |  # 질문 글쓴이
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이
        ).distinct()
    paginator = Paginator(question_list, 5)  # 페이지당 5개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'categories': categories, 'category': category}
    return render(request, 'pybo/question_list.html', context)
