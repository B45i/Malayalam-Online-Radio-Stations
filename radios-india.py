import requests
import re
import json


url = 'https://radiosindia.com/malayalamradio.html'

f = open('radiosindia-malayalam,json','w+')
channel_dict = {}

r = requests.get(url, timeout=5)

channels = re.findall('<a\shref="([^"]+)"><img\sheight="100"', r.text)
for channel in channels:
	print('Processing {}'.format(channel))
	u = 'https://radiosindia.com/{}'.format(channel)
	r = requests.get(u, timeout=100)
	streams = re.search('<source\ssrc="([^"]+)"', r.text)
	channel_names = re.search('<h2>(.*?)</h2>', r.text)
	if streams:
		channel_dict[channel_names.group(1)] = streams.group(1)
	else:
		print('Channel {} failed'.format(u))

f.write(json.dumps(channel_dict))