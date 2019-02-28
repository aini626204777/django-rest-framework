import requests
import re
import pymysql

url = 'http://kaijiang.500.com/static/info/kaijiang/xml/ssq/list.xml?_A=BLWXUIYA1546584359929'

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='1807_spider_db', )

cursor = connection.cursor()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
reponse = requests.get(url=url, headers=headers)

pattern = re.compile(r'<row.*?opencode="(.*?)".*?opentime="(.*?)"')
list = pattern.findall(reponse.text)


#13,17,20,21,22,27|01
for t in list:
    x, y = t
    red,blue = x.split("|")
    print(red,blue,y)
