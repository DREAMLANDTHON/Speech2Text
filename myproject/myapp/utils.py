# myapp/utils.py

import requests

def get_chat_response(input_text):
    api_endpoint = ""  # ChatGPT API의 엔드포인트 주소
    api_key = "YOUR_API_KEY"  # ChatGPT API의 API 키

    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    data = {
        "input_text": input_text,
    }

    response = requests.post(api_endpoint, headers=headers, json=data)

    if response.status_code == 200:
        return response.json().get("output_text")
    else:
        return "API 호출에 실패했습니다."