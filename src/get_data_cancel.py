import requests
import pandas as pd

def get_data():
    servicekey = 'n10J1U3TXuzNqRQkALNyYk8YzRRN2g8s/z2kM7omSrzjBvLfPkim/g/Oi4fp+y1Qu6bDPnlpD0uw5tOlTyl3/A=='
    url = 'http://apis.data.go.kr/B551172/Lung04/luAlchbyType'
    params = {
        'serviceKey': servicekey,
        'pageNo': 1,
        'numOfRows': 50,
        'centerNm': '국립암센터',
        'fromYear': 2010,
        'toYear': 2019,
        'type': 'json'
    }

    response = requests.get(url, params=params)
    results = []
    if response.status_code == 200:
        # return response.json()
        data = response.json()
        items = data['items']

        for item in items:
            statsMetaNo = item['statsMetaNo']
            centerNm = item['centerNm']
            critYr = item['critYr']
            ptAge= item['ptAge']
            ptSexCd= item['ptSexCd']
            statsTrgtNm= item['statsTrgtNm']
            ncsNmvl= item['ncsNmvl']
            wholNcsDnmvl= item['wholNcsDnmvl']
            ptCntNmvl= item['ptCntNmvl']
            wholPtCntDnmvl= item['wholPtCntDnmvl']
            
            
            results.append((statsMetaNo, centerNm, critYr, ptAge, ptSexCd, statsTrgtNm,
                            ncsNmvl, wholNcsDnmvl,ptCntNmvl,wholPtCntDnmvl))
    
    # else:
    #     print(f"Error {response.status_code}: {response.text}")
    return results

if __name__=='__main__':

    data = get_data()
    print(data)
    columns = ['statsMetaNo', 'centerNm', 'critYr', 'ptAge', 'ptSexCd', 'statsTrgtNm', 'ncsNmvl', 
            'wholNcsDnmvl', 'ptCntNmvl', 'wholPtCntDnmvl']
    df = pd.DataFrame(data, columns=columns)

    # DataFrame을 엑셀 파일로 저장
    df.to_excel('data/cancel_data.xlsx', index=False)
    print("Data saved to 'data_output.xlsx'")
