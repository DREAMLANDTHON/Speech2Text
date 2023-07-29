# myapp/views.py

from django.shortcuts import render
from .utils import get_chat_response
from django.http import JsonResponse
from . import stt
import time
from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import HttpResponse

import openai
from .models import Saved  # YourModel은 저장하고자 하는 모델명으로 대체해야 합니다.


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def home(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        if user_input:
            chat_response = get_chat_response(user_input)
            return render(request, "myapp/home.html", {"user_input": user_input, "chat_response": chat_response})

    return render(request, "myapp/home.html")


def subpage_view(request):
    # Your view logic here (e.g., fetch data from the database, etc.)
    return render(request, 'myapp/indexx.html')
# def my_function(request):
#     # 파이썬 함수 실행 로직을 작성하고 결과를 얻어옴

#     start_time = time.time()
#     result = ""
#     cum_result = ""
    
#     result = stt.do()
#     cum_result += result

#     #time.sleep(1)  # 1초 대기
#     return JsonResponse({'result': result})

# views.py

def my_function(request):
    # 파이썬 함수 실행 로직을 작성하고 결과를 얻어옴

    result = stt.do()
    return JsonResponse({'result': result})

@csrf_exempt
def get_text_value(request):
    if request.method == 'POST': #  and is_ajax(request)
        text_value = request.POST.get('text_value', '')
        # 파이썬 함수에서 텍스트 값을 처리하고 출력
        my_variable = process_text_function(text_value)
        
    # my_variable
    return JsonResponse({'ans': my_variable}) 
    
def save_result_to_db(request):
    if request.method == "POST":
        result = request.POST.get("result")  # 클라이언트에서 전송한 결과값을 가져옴

        # DB에 결과값 저장
        Saved.objects.create(result=result)
        return JsonResponse({"message": "Result saved successfully."})

def show_saved_results(request):
    saved_results = Saved.objects.all()
    return render(request, "myapp/saved_results.html", {"saved_results": saved_results})

    return JsonResponse({"error": "Invalid request method."}, status=400)

def process_text_function(text):
    print("!!:" + text)
    openai.api_key = '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'

    completion = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {'role': 'user', 'content': "다음 내용을 쉽게 요약해서 알려줘. "+text}
    ],
    temperature = 0  
    )

 
    ans = completion.choices[0].message.content
    print(ans)
    return ans

    