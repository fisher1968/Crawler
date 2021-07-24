import requests
from bs4 import BeautifulSoup
import urllib.parse

import xlwt
import xlrd


url='https://accounts.douban.com/j/mobile/login/basic'
header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
        'Origin': 'https://accounts.douban.com',
 'content-Type':'application/x-www-form-urlencoded',
 'x-requested-with':'XMLHttpRequest',
 'accept':'application/json',
 'accept-encoding':'gzip, deflate, br',
 'accept-language':'zh-CN,zh;q=0.9',
 'connection': 'keep-alive'
 ,'Host': 'accounts.douban.com'
 }
data={
    'ck':'',
    'name':'huagnziqun@163.com',
    'password':'Hzqlly1985',
    'remember':'false',
    'ticket':''
}
def login(username,password):
    global  data
    data['name']=username
    data['password']=password
    data=urllib.parse.urlencode(data)
    print(data)
    req=requests.post(url,headers=header,data=data,verify=False)
    html=requests.post(url,headers=header,data=data,verify=False).content.decode('utf-8')
    print(req)
    print(html)
    cookies = requests.utils.dict_from_cookiejar(req.cookies)
    print(cookies)
    return cookies

if __name__ == '__main__':
    username = input('输入账号：')
    password = input('输入密码：')
    cookies = login(username, password)
   