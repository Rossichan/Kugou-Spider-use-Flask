# coding=utf-8
import sys
from flask import Flask
from flask_cors import *
from imp import reload
#导入render_template
from flask import request,render_template
from KuGou_Spid import Music_download

reload(sys)

app = Flask(__name__)
CORS(app)
#修饰器实现路由
#路由127.0.0.1.5000
@app.route('/', methods=['GET', 'POST'])

def search():
    if request.method == 'GET':
        return render_template('search.html')

    elif request.method == 'POST':
        keyword = request.form.get('keyword')
        items = Music_download.HighSearch(keyword)
        if items != None:
            return render_template('list.html', list=items)
        else:
            return '找不到！！！不支持英文'

    else:
        return render_template('404.html')




if __name__ == '__main__':
    app.run(debug=True)
    # free_proxyIP.main()
