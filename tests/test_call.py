from src.mov.api import get_key, req, req2dataframe

def test_req2dataframe():
	l = reqdataframe()
	assert len(l) > 0
	v = l[0]
	assert 'rnum' in v.keys()
	assert v['rnum'] == 1

def test_비밀키_호출():
	pass

def test_통신_테스트():
	pass

