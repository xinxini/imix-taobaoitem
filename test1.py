#encoding=utf-8
import re
import requests
from retest import fun2
web=requests.get('https://s.taobao.com/search?q=%E8%A3%99&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170305')
content=web.content
p=re.compile(r'raw_title":"(.*?)","pic_url',re.S)
results=re.findall(p,content)

for i in results:
    print i
    fun2(i)









