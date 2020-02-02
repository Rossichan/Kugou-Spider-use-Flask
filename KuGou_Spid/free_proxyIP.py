from multiprocessing.dummy import Pool as ThreadPool
import requests
from lxml import etree
import time
import csv
import random

url = 'https://www.kuaidaili.com/free/inha/{}/'
alive_ip = []


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }
        reponse = requests.get(url,headers = headers)
        if reponse.status_code == 200:
           return reponse.text
        return None
    except requests.RequestException:
        return None

def get_one_parse(url):
   with open('IP/456.txt', 'a+') as f: # 保存在相应的文件里
       print(url) # 看爬取到第几页来了
       html = get_one_page(url)
       html = etree.HTML(html)# 从获得的html页面中分析提取出所需要的数据
       IP = html.xpath('.//*[@id="list"]/table/tbody//td[1]/text()') # 使用相对路径（//）查找所有id="list"的标签
       ports = html.xpath('.//*[@id="list"]/table/tbody//td[2]/text()')# 这是 端口位置
       for (ip,port) in zip(IP,ports): # 保存
           ip = ip +':' +  port
           print("测试：{}".format(ip))
           f.write(ip + '\n')

def validate(ip):
   IP = {'http':ip} #指定对应的 IP 进行访问网址
   try:
       r = requests.get('http://trackercdn.kugou.com/i/v2/?appid=1005&pid=2&cmd=25&behavior=play', proxies=IP, timeout=3)# proxies 设定对应的代理 IP 进行访问， timeout 设定相应的时间之后停止等待响应
       if r.status_code == 200:
           print("成功:{}".format(ip))
           alive_ip.append(ip) # 有效的 IP 则添加进去
   except:
       print("无效")

def save(writer):
       for ip in alive_ip:
           writer.writerow([ip])
           print(ip)
       print("成功保存所有有效 ip ")

def check(writer):
    with open('IP/456.txt', 'r') as f:
        lines = f.readlines()
        # 我们去掉lines每一项后面的\n\r之类的空格
        # 生成一个新的列表！
        ips = list(map(lambda x: x.strip(), [line for line in lines]))  # strip() 方法用于移除字符串头尾指定的字符，默认就是空格或换行符。
        pool = ThreadPool(20)  # 多线程 设置并发数量！
        pool.map(validate, ips)  # 用 map 简捷实现 Python 程序并行化
        save(writer)  # 保存能用的 IP

def get_proxy():
    with open('KuGou_Spid/IP/validate.csv',mode='r',encoding='utf-8',newline='') as f:
        datas = f.readlines()
    ran_num = random.choice(datas)
    ip = ran_num.strip().split('/r')
    proxies = {'http://':'http://'+ ip[0]}
    return proxies


def main():
    csv_file = open('IP/validate.csv', 'w', newline='')
    writer = csv.writer(csv_file)
    writer.writerow(['ip'])
    url = 'https://www.kuaidaili.com/free/inha/{}/'  # 这是网站的 url
    for i in range(1, 50):  # 爬取四十页
        time.sleep(1)  # 休息 1 秒
        get_one_parse(url.format(i))
    check(writer)
    csv_file.close()

if __name__ == '__main__':
    #check()
    #proxyip()
    main()
