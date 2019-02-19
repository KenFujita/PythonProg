import urllib.request
import urllib.parse
import json
import csv

'''
        #################
        #   dmmapi.py   #
        #################

        指定した女優の作品上位5つのサムネを取得するプログラム

'''


url = "https://api.dmm.com/affiliate/v3/ItemList?"

csv_w = ""

param = {
    'api_id' : 'my-dmm-api-key',
    'affiliate_id' : 'my-affiliate-id',
    'site' : 'FANZA',
    'service' : 'digital',
    'floor' : 'videoa',
    'hits' : '5',
    'sort' : 'rank',
    'keyword' : 'actor-name',
    'output' : 'json'
}

res_sum = param['hits']
paramStr = urllib.parse.urlencode(param)

readObj = urllib.request.urlopen(url+paramStr)

response = json.loads(readObj.read().decode('utf-8'))

res = response['result']
with open(param['keyword']+'_pictures.csv','w') as f:
    writer = csv.writer(f)
    for i,av_l in enumerate(res):
        print(res['items'][i]['title'])
        #print(res['items'][i]['sampleImageURL']['sample_s'])
        for j,thumb in enumerate(res['items'][i]['sampleImageURL']['sample_s']['image']):
            writer.writerow([thumb])
            print(str(j)+":"+thumb)
