import re
import requests

for i in range(1, 1000):
	r = requests.post('http://malayalamonlineradio.in/getstation.php', data={'stationId': i})
	if r.text:
		print(re.search('src="([^"]+)"', r.text).group(1))
	else:
		break