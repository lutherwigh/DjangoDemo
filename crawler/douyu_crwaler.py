import requests
import re

dota2_url = 'https://m.douyu.com/api/room/list?page=1&type=DOTA2'
# 'https://www.douyu.com/g_DOTA2'


def get_dota2_channels():
    session = requests.Session()
    response = session.get(dota2_url, verify=False)

    write_to_localdata(response)

    # # 获取dota2 channel 第一页json列表
    # list_json = re.match('<script>window.$DATA([\s\S]*?)<\/script>',str(response.content))
    # print(list_json)



def write_to_localdata(response):
    with open(file='crawler\\data\\douyu_response.html', mode='a+', encoding='UTF-8') as f:
        f.write(response.content.decode('UTF-8'))

get_dota2_channels()