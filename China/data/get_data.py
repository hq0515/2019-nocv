import requests
import json

class Data():

    def __init__(self):
        self.url='https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    
    def get_data(self):
        res=requests.get(self.url,timeout=30)
        res.encoding='utf-8'

        da=json.loads(res.text)
        all_da=json.loads(da['data'])

        return all_da

if __name__=='__main__':
    ncovdata=Data()
    ncovdata.get_data
            

