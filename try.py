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
    'publication': 'ICML 2019',
    'urllist': ['https://dblp.org/db/conf/icml/icml2019'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
    'pagepatten': '<div class="head"><a href="(.*?)"><img alt="" src="https://dblp.org/img/paper.dark.hollow.16x16.png" class="icon" itemprop="image"></a></div>',
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


