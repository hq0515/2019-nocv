import requests
import json

def get_data_china():
    res = requests.get('https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5',timeout=30)
    res.encoding='utf-8'
    html_data=json.loads(res.text)
    get_data=json.loads(html_data['data'])
    areaTree = get_data['areaTree'][0]['children']
    province_name = list()
    province_total_confirm = list()
    for province in areaTree:
        province_name.append(province['name'])
        province_total_confirm.append(province['total']['confirm'])
    province_dict={'name': province_name, 'value': province_total_confirm}
    return province_dict

def get_data_world():
    res=requests.get('https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign')
    res.encoding='utf-8'
    html_data=json.loads(res.text)
    get_data=json.loads(html_data['data'])
    country_name=list()
    country_total_confirm=list()
    for index in range(len(get_data['foreignList'])):
        country_name.append(get_data['foreignList'][index]['name'])
        country_total_confirm.append(get_data['foreignList'][index]['confirm'])
    r = requests.get('https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5',timeout=30)
    r.encoding='utf-8'
    h=json.loads(r.text)
    g=json.loads(h['data'])
    country_name.append('中国')
    country_total_confirm.append(g['chinaTotal']['confirm'])
    country_dict={'name': country_name, 'value': country_total_confirm}
    return country_dict

def get_time():
    res = requests.get('https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5',timeout=30)
    res.encoding='utf-8'
    html_data=json.loads(res.text)
    get_data=json.loads(html_data['data'])
    print(get_data['lastUpdateTime'])
    return get_data['lastUpdateTime']


