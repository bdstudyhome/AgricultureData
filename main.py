from urllib import request
from urllib.parse import urlencode, quote_plus, unquote
from urllib.request import urlopen
import json
import urllib
import pandas as pd
from pandas import json_normalize

date_list = pd.date_range('2010-01-01', periods=365).strftime('%Y%m%d').tolist()
area_list = ['4825000000', '4136000088', '4420000088', '4571000088', '4579000088', '4580000088', '2700000088', '2600000088',
              '4128100001', '4131000001', '4215000002', '4421000001', '4150000088', '4420000088', '4571000088', '4580000088',
              '4155000000', '4167000001', '4311300001', '4421000001', '4825000000', '4150000088', '4276000088', '4420000088',
              '4571000088', '4579000088', '4580000088', '2600000088', '4128100001', '4155000000', '4167000001', '4215000002',
              '4421000001', '4825000000', '4687000088', '2600000088', '4690000001', '4691000001']
area_list = ['4825000000', '4136000088']

url = 'http://apis.data.go.kr/1360000/FmlandWthrInfoService/getDayStatistics'

# checkpoint = 0
for ymd in date_list:
    for area in area_list:
        queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'nqe5J5wrz1iVkUH57dST%2BEuSNPky6pZTB28fIiAlfMTAhs2P5Xh3ZsC0IGNatBap8oGWW9rEoarBvV9ojCOSvQ%3D%3D',
                                        quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('dataType') : 'JSON', quote_plus('ST_YMD') : ymd, quote_plus('ED_YMD') : ymd, quote_plus('AREA_ID') : area, quote_plus('PA_CROP_SPE_ID') : 'PA090101' })
        req = urllib.request.Request(url + unquote(queryParams))
        req.get_method = lambda: 'GET'
        response_body = urlopen(req).read()
        response_body = response_body.decode('UTF-8', 'strict')
        data = json.loads(response_body)

        if(data['response']['header']['resultCode']) == '00':
            print(data['response']['body']['items']['item'][0])
#            if checkpoint == 0:
#                df = json_normalize(data['response']['body']['items']['item'])
#                checkpoint += 1
#            else:
#                temp = json_normalize(data['response']['body']['items']['item'])
#                df = df.append(temp)


# df.to_csv("data.csv")