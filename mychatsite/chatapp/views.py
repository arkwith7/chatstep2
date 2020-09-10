from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
context = {}

# def index(request):
#     msg = '박형식 홈페이지'
#     return render(request, 'chatapp/index.html', {'message': msg})

def index(request):
    template = loader.get_template('chatapp/base_contents_kr.html')
#    template = loader.get_template('base_contents.html')
    context = {
#         'login_success' : False,
#         'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

def chat_home(request):
    template = loader.get_template('chatapp/chat_home_screen.html')
    context = {
        'login_success' : False,
        'initMessages' : ["아크위드 채팅 홈페이지에 오신것을 환영합니다",
                          "아크위드 홈페이지 설명 챗봇이 회사의  vision, mission, 제품, 서비스, 주요기술, 연락처에 대해 답변합니다."]
    }
    return HttpResponse(template.render(context, request))

def popup_chat_home(request):
    template = loader.get_template('chatapp/popup_chat_home_screen.html')
    context = {
        'login_success' : False,
        'initMessages' : ["아크위드 채팅 홈페이지에 오신것을 환영합니다",
                          "아크위드 홈페이지 설명 챗봇이 회사의  vision, mission, 제품, 서비스, 주요기술, 연락처에 대해 답변합니다."]
    }
    return HttpResponse(template.render(context, request))

def call_chatbot(request):
    if request.method == 'POST':
        if request.is_ajax():
            userID = request.POST['user']
            sentence = request.POST['message']
            # logger.debug("question[{}]".format(sentence))
            # answer = clean_up_sentence(sentence)
            # answer = bot.response(sentence, userID)
            # answer = bot.get_answer(sentence, userID)
            answer = sentence
            # logger.debug("answer[{}]".format(answer))
            return HttpResponse(answer)
     
    return render(request)
