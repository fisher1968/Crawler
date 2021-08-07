import requests

headers = {
    'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
data = {
    'ck': '',
    'name': 'huangziqun@163.com', # 输入你豆瓣的账户名
    'password': 'Hzqlly198', # 输入你豆瓣的密码
    'remember': 'false',
    'ticket': ''
}

s = requests.Session()


def login_douban():
    login_url = 'https://accounts.douban.com/j/mobile/login/basic'
    try:
        html = s.post(url=login_url, headers=headers, data=data).content.decode('utf-8')
        print(html)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    login_douban()
