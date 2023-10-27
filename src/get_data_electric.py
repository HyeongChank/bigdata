import requests

def get_power_usage(year, month, metroCd, cityCd, bizCd, apiKey):
    # API URL
    url = "https://bigdata.kepco.co.kr/openapi/v1/powerUsage/industryType.do"
    
    # Query Parameters
    params = {
        "year": year,
        "month": month,
        "metroCd": metroCd,
        "cityCd": cityCd,
        "bizCd": bizCd,
        "apiKey": apiKey,
        "returnType": "json"
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
data = get_power_usage("2021", "09", "11", "11", "C", api_key)
print(data)
