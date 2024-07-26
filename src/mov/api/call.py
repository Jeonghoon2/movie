def req(dt="20120101"):
	base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml "
	key = "6158692ade44de1857753bae9741d704"

	url = f"{base_url}?key={key}&targetDt={dt}"
	print(url)

req()

