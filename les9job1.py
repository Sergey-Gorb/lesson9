import json
import requests
import operator

resp_dict = {}
token ='2619421814940190'
api_path = 'https://superheroapi.com/api'
names = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}
for name in names:
    params = '/' + token + '/search/' + name
    request = api_path + params
    resp = requests.get(request)
    resp_dict = json.loads(resp.text)
    if resp_dict['response'] == 'success':
        names[name] = int(resp_dict['results'][0]['powerstats']['intelligence'])
#    print(resp.text)
sorted_tuple = sorted(names.items(), key=operator.itemgetter(1))

print(sorted_tuple[-1])
