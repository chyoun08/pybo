from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question

from django.db.models import Q, Count

def index(request):
    #return HttpResponse("お早うございます　こちらはPIBOです")
    """
    pybo 목록 출력
    """

    """
    #order_by를 통해 question테이블의 목록을 정리해서 가져올수있다.이때 "-"가있음으로 역순으로 가져온다
    question_list = Question.objects.order_by('-create_date')
    #question_list로 가져온 리스트값을 context에 파싱해서 보내준다.(MVC생각하면됨)
    context ={'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)
    """

    #현제 페이지
    page = request.GET.get('page','1') #기본 페이지
    kw = request.GET.get('kw','') #검색어

    #출력될 페이지 리스트
    question_list = Question.objects.order_by('-create_date')

    so = request.GET.get('so', 'recent')  # 정렬기준

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        question_list = Question.objects.order_by('-create_date')

    #조회 입력받은kw에따라 출력될 question_list를 찾아준다.
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | #제목 검색
            Q(content__icontains=kw) | #내용 검색
            Q(author__username__icontains=kw)| #질문 글쓴이 검색
            Q(answer__author__username__icontains=kw) #답변 글쓴이 검색
        ).distinct()

    #페이징 처리
    paginator = Paginator(question_list, 3)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    #question객체 받아오는 방법
    #question = Question.objects.get(id=question_id)
    #question객체를 받아오는데 없을경우 404전송 이때는 기본키값을 이용한다
    question = get_object_or_404(Question,pk=question_id)
    context = {'question': question}
    
    return render(request, 'pybo/question_detail.html', context)