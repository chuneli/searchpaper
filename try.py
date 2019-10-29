#

import requests
import codecs
import json
from requests.exceptions import RequestException
import re
import multiprocessing

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            response = response.text
            return response
        else:
            return None
    except RequestException:
        return None


resouce={
    'publication': 'EMNLP 2019',
    'urllist': ['https://www.emnlp-ijcnlp2019.org/program/accepted/'],
    'titlepatten': '<li><span style="color:cornflowerblue">(.*?)</span>',
}
publication=resouce['publication']
urllist=resouce['urllist']
titlepatten=resouce['titlepatten']
keyword='meta'

for url in urllist:
    html = get_one_page(url)
    #print(html)
    pattern = re.compile(titlepatten, re.S)
    items = re.findall(pattern, html)
    for item in items:
        if item.lower().find(keyword.lower()) > -1:
           print(item.strip()+'\n')


