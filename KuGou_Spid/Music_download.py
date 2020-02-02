# coding=utf-8
import copy
import hashlib
from KuGou_Spid import web_request
from KuGou_Spid import Music_Search

# V2版系统,pc版,加密方式为md5(hash +"kgcloudv2")
Music_api_1 = 'http://trackercdnbj.kugou.com/i/v2/?cmd=23&pid=1&behavior=download'
# V2版系统,手机版,加密方式为md5(hash +"kgcloudv2") （备用）
Music_api_2 = 'http://trackercdn.kugou.com/i/v2/?appid=1005&pid=2&cmd=25&behavior=play'
# 老版系统,加密方式为md5(hash +"kgcloud")（备用）
Music_api_3 = 'http://trackercdn.kugou.com/i/?cmd=4&pid=1&forceDown=0&vip=1'
def V2Md5(Hash):  # 用于生成key,适用于V2版酷狗系统
    return hashlib.md5((Hash + 'kgcloudv2').encode("utf-8")).hexdigest()
def Md5(Hash):  # 用于老版酷狗系统
    return hashlib.md5((Hash + 'kgcloud').encode("utf-8")).hexdigest()
def HighSearch(keyword):
    music_list = Music_Search.search(keyword)
    if music_list is not None:
        item, items = {}, []
        for music in music_list:
            SQHash = str.lower(music['SQHash'])
            HQHash = str.lower(music['HQHash'])
            key_new_SQ = V2Md5(SQHash)  # 生成v2系统key
            key_new_HQ = V2Md5(HQHash)
            try:
                DownUrl = web_request.parse(Music_api_2 + '&hash=%s&key=%s' % (SQHash, key_new_SQ))
                if DownUrl['status'] == 2:
                    DownUrl = web_request.parse(Music_api_2 + '&hash=%s&key=%s' % (HQHash, key_new_HQ))
                item['Song'] = music['Song'] # 歌名
                item['Singer'] = music['Singer']  # 歌手
                item['url'] = DownUrl['url'][0]
                item['Size'] = music['Size']
                item['minute'] = music['minute']
                item['second'] = music['second']
                items.append(copy.deepcopy(item))
            except KeyError:
                pass
        return items
if __name__ == '__main__':
    HighSearch()
