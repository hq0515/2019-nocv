import get_data
import json

class ProvinceData():

    def __init__(self):
        self.data=get_data.Data()
        self.all_data=self.data.get_data()

    def province_total_data(self):
        areaTree = self.all_data['areaTree'][0]['children']
        province_name = list()
        province_total_confirm = list()
        province_total_suspect = list()
        province_total_dead = list()
        province_total_heal = list()
        for province in areaTree:
            province_name.append(province['name'])
            province_total_confirm.append(province['total']['confirm'])
            province_total_suspect.append(province['total']['suspect'])
            province_total_dead.append(province['total']['dead'])
            province_total_heal.append(province['total']['heal'])
        province_total_confirm_dict = {'name': province_name, 'value': province_total_confirm}
        print(province_total_confirm_dict)
        with open('province_total.json', 'w', encoding='utf-8') as f:
            json.dump(province_total_confirm_dict,f,ensure_ascii=False)
        return province_name
    def province_today_data(self):
        '''获取各省今日数据'''
        areaTree = self.all_data['areaTree'][0]['children']
        province_name = list()
        province_today_confirm = list()
        province_today_suspect = list()
        province_today_dead = list()
        province_today_heal = list()
        for province in areaTree:
            province_name.append(province['name'])
            province_today_confirm.append(province['today']['confirm'])
            # province_today_suspect.append(province['today']['suspect'])  # 目前疑似病例数据已经没了可以注销该栏
            province_today_dead.append(province['total']['dead'])
            province_today_heal.append(province['total']['heal'])
        # print(province_today_confirm)

if __name__=='__main__':
    province_data=ProvinceData()
    province_data.province_total_data()