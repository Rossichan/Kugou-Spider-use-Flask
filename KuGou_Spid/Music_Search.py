import copy
from KuGou_Spid import web_request

def search(keyword):
    search_url = 'http://mobilecdn.kugou.com/api/v3/search/song?format=json&keyword={}&page=1'.format(keyword)
    # 这里需要判断一下，ip与搜索字段可能会限制搜索，total进行判断
    total = web_request.parse(search_url)['data']['total']
    if total != 0:
        search_total_url = search_url + '&pagesize=%d' % total
        music_list = web_request.parse(search_total_url)['data']['info']  #这是字典结构
        item, items = {}, []
        for music in music_list:
            if music['sqhash'] != '0'*32:
                item['Song'] = music['songname_original']  # 歌名
                item['Singer'] = music['singername']  # 歌手
                item['SQHash'] = music['sqhash'] # 歌曲无损hash
                item['HQHash'] = music['hash']  # 歌曲高清hash
                item['Size'] = str(round((music['sqfilesize']/1024)/1024,2))+'M'
                item['minute'] = str(int(music['duration']/60))
                if(music['duration']%60<10):
                    item['second'] = '0'+str(music['duration'] % 60)
                else:
                    item['second'] = str(music['duration'] % 60)
                items.append(copy.deepcopy(item))
        return items
    else:
        return None

if __name__ == '__main__':
    search()

