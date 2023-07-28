# myapp/views.py

from django.shortcuts import render
from .utils import get_chat_response
from django.http import JsonResponse
from . import stt
import time

def home(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        if user_input:
            chat_response = get_chat_response(user_input)
            return render(request, "myapp/home.html", {"user_input": user_input, "chat_response": chat_response})

    return render(request, "myapp/home.html")

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
myresult = ""
def my_function(request):
    # 파이썬 함수 실행 로직을 작성하고 결과를 얻어옴

    result = stt.do()
    return JsonResponse({'result': myresult})
