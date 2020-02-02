# coding=utf-8
import requests
import json
from KuGou_Spid import free_proxyIP

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/63.0.3239.132 Safari/537.36',
}
proxy = free_proxyIP.get_proxy()
def parse(url):
    try:
        ret = json.loads(requests.get(url, headers=headers,proxies=proxy,timeout=5).text)
        return ret
    except Exception as e:
        print(e)
    else:
        ret = json.loads(requests.get(url, headers=headers,timeout=5).text)
    # 返回的是已经转换过后的字典数据
        return ret


if __name__ == '__main__':
    parse()
