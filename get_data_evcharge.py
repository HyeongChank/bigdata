import requests

def get_ev_charge_data(metroCd, cityCd, apiKey, returnType="json"):
    # API URL
    url = "https://bigdata.kepco.co.kr/openapi/v1/EVcharge.do"
    
    # Query Parameters
    params = {
        "metroCd": metroCd,
        "cityCd": cityCd,
        "apiKey": apiKey,
        "returnType": returnType
    }
    
    # API 요청
    response = requests.get(url, params=params)
    
    # JSON 응답 확인
    if response.status_code == 200:
        return response.json()["data"]
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# API 호출 예시
api_key = "R9EY8IgX6Fl74564covwWgzB3xBs4wz7Z5h3Xb19"
data = get_ev_charge_data("21", "", api_key)
print(data)
