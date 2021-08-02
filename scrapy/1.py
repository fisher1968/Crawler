# encoding: utf-8
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from lxml import etree
import pandas as pd
import numpy as np



def get_tracks(distance, rate=0.6, t=0.2, v=0):
    """
    将distance分割成小段的距离
    :param distance: 总距离
    :param rate: 加速减速的临界比例
    :param a1: 加速度
    :param a2: 减速度
    :param t: 单位时间
    :param t: 初始速度
    :return: 小段的距离集合
    """
    tracks = []
    # 加速减速的临界值
    mid = rate * distance
    # 当前位移
    s = 0
    # 循环
    while s < distance:
        # 初始速度
        v0 = v
        if s < mid:
            a = 20
        else:
            a = -3
        # 计算当前t时间段走的距离
        s0 = v0 * t + 0.5 * a * t * t
        # 计算当前速度
        v = v0 + a * t
        # 四舍五入距离，因为像素没有小数
        tracks.append(round(s0))
        # 计算当前距离
        s += s0


    return tracks




def slide(driver):
    """滑动验证码"""
    # 切换iframe
    driver.switch_to.frame(1)
    #找到滑块
    block = driver.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')
    #找到刷新
    reload = driver.find_element_by_xpath('//*[@id="reload"]')
    while True:
        # 摁下滑块
        ActionChains(driver).click_and_hold(block).perform()
        # 移动
        ActionChains(driver).move_by_offset(180, 0).perform()
        #获取位移
        tracks = get_tracks(30)
        #循环
        for track in tracks:
            #移动
            ActionChains(driver).move_by_offset(track, 0).perform()
        # 释放
        ActionChains(driver).release().perform()
        #停一下
        time.sleep(2)
        #判断
        if driver.title == "登录豆瓣":
            print("失败...再来一次...")
            #单击刷新按钮刷新
            time.sleep(5)
            reload.click()
            # 停一下
            time.sleep(5)
        else:
            break
def l_j(a, b, c):  # 定义一个连接三个dataframe的函数
    d = pd.concat([a, b, c], axis=1)

def main():
    """主程序"""
    url = "https://accounts.douban.com/passport/login"
    driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[1]/ul[1]/li[2]').click()
    driver.find_element_by_xpath('//*[@id="username"]').send_keys("huangziqun@163.com")
    driver.find_element_by_xpath('//*[@id="password"]').send_keys("Hzqlly1985")
    driver.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[2]/div[1]/div[4]/a').click()
    # 停一下，等待出现
    time.sleep(2)
    #滑动验证码
    # slide(driver)
    print("成功")

    # 点击我的电影页面
   
    driver.find_element_by_xpath('//*[@id="db-nav-sns"]/div/div/div[3]/ul/li[2]/a').click()
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="movie"]/h2/span/a[2]').click()
    time.sleep(2)

    handles = driver.window_handles
    driver.switch_to.window(handles[-1])
    time.sleep(2)


    film_name = []
    film_see_time = []
    film_star = []

    for i in range(0, 10):
        if i == 0:
            web_ad = driver.current_url
            # print('web_ad',web_ad)
            cookies = driver.get_cookies()
            cookie_dict = {}
            for j in cookies:
             cookie_dict[j["name"]] = j["value"]
            ua_pretend = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
            react_data = requests.get(url=web_ad, headers=ua_pretend, cookies=cookie_dict).text
            # print('react_data',react_data)
            analysis = etree.HTML(react_data)
            film_name.append(analysis.xpath('//li/a/em/text()'))
            print(film_name)
            film_name = film_name[0]
            film_name = [i.split('/')[0] for i in film_name]
            df1 = pd.DataFrame(film_name)
            film_see_time.append(analysis.xpath('//li/span[@class="date"]/text()'))
            film_see_time = film_see_time[0]
            df2 = pd.DataFrame(film_see_time)
            film_star.append(analysis.xpath('//li[3]//@class'))
            film_star = film_star[0]
            film_star = [i for i in film_star if 'rating' in i]
            film_star = [i.split('-')[-2][-1] for i in film_star]
            df3 = pd.DataFrame(film_star)
            f_l = pd.concat([df1, df2, df3], axis=1)
            print(f_l)
            f_l.to_csv('D:\my_db_film.csv', header=['filenam', 'filetime', 'star'], index=False, encoding='ANSI', mode='a')
        else:
            film_name = []
            film_see_time = []
            film_star = []
            driver.find_element_by_xpath(f'//*[@id="content"]/div[2]/div[1]/div[3]/a[{i}]').click()
            time.sleep(2)
            web_ad = driver.current_url
            ua_pretend = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
            react_data = requests.get(url=web_ad, headers=ua_pretend, cookies=cookie_dict).text
            analysis = etree.HTML(react_data)
            film_name.append(analysis.xpath('//li/a/em/text()'))
            film_name = film_name[0]
            film_name = [i.split('/')[0] for i in film_name]
            df1 = pd.DataFrame(film_name)
            film_see_time.append(analysis.xpath('//li/span[@class="date"]/text()'))
            film_see_time = film_see_time[0]
            df2 = pd.DataFrame(film_see_time)

            film_star.append(analysis.xpath('//li[3]//@class'))
            film_star = film_star[0]
            film_star = [i for i in film_star if 'rating' in i]
            film_star = [i.split('-')[0][-1] for i in film_star]
            df3 = pd.DataFrame(film_star)
            new = l_j(df1, df2, df3)
            new = np.array(new)
            new = pd.DataFrame(new)
            new.to_csv('D:/my_db_film.csv', header=False, index=False, encoding='ANSI', mode='a')



if __name__ == '__main__':
    main()

    
    
    
