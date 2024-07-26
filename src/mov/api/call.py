import requests
import os

def req2dataframe():
	_, data = req()
	l = data['boxOfficeResult']['dailyBoxOfficeList']
	retun l
	
def get_key():
	key = os.getenv('MOVIE_API_KEY')
	return key

def gen_req_url(dt="20120101"):
	base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml "
	key = "6158692ade44de1857753bae9741d704"

	url = f"{base_url}?key={key}&targetDt={dt}"
	return url

def req(url:str):
	res = request.get(url)

	code = res.status_code()
	data = res.json()

	return [data, code] 

def main():
	print("start")
	url = gen_req_url
	res = req(url)

	print(f"""
	{res[0]}

	{res[1]}

	"""
	)
