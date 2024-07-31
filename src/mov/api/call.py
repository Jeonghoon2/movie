import requests
import os
import pandas as pd


def get_url_params(url_params={}):
    return url_params


def echo(yaho):
    return yaho


def apply_type2df(load_dt="20120101", path="~/tmp/test_parquet"):
    df = pd.read_parquet(f'{path}/load_dt={load_dt}')

    num_cols = ['rnum', 'rank', 'rankInten', 'salesAmt', 'audiCnt',
                'audiAcc', 'scrnCnt', 'showCnt', 'salesShare', 'salesInten',
                'salesChange', 'audiInten', 'audiChange']

    df[num_cols] = df[num_cols].apply(pd.to_numeric)

    return df


def save2df(load_dt='20120101', url_params={}):
    """airflow 호출 지점"""
    df = list2df(load_dt, url_params)
    # df 에 load_dt 컬럼 추가 (조회 일자 YYYYMMDD 형식 으로)
    # 아래 파일 저장시 load_dt 기분으로 파티셔닝
    df['load_dt'] = load_dt

    partition = [
        'load_dt'
    ]

    for k, v in url_params.items():
        df[k] = v
        partition.append(k)

    df.to_parquet('~/tmp/test_parquet', partition_cols=partition)
    return df


def list2df(load_dt='20120101', url_params={}):
    l = req2list(load_dt, url_params)
    df = pd.DataFrame(l)
    return df


def req2list(load_dt='20120101', url_params={}) -> list:
    _, data = req(load_dt, url_params)
    l = data['boxOfficeResult']['dailyBoxOfficeList']
    return l


def get_key():
    key = os.getenv('MOVIE_API_KEY')
    return key


def req(load_dt="20120101", url_params={}):
    url = gen_url(load_dt, url_params)
    r = requests.get(url)
    code = r.status_code
    data = r.json()
    print(data)
    return code, data


def gen_url(dt="20120101", url_params={}):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"

    for k, v in url_params.items():
        url = url + f"&{k}={v}"

    return url
