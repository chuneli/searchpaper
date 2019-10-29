from scrapy.selector import Selector
import requests
from requests.exceptions import RequestException

resouce = {
    'publication': 'ICML 2019',
    'urllist': ['https://dblp.org/db/conf/icml/icml2019'],
    'titlepatten': '<span class="title" itemprop="name">(.*?).</span> ',
    'pagepatten': '<div class="head"><a href="(.*?)"><img alt="" src="https://dblp.org/img/paper.dark.hollow.16x16.png" class="icon" itemprop="image"></a></div>',
}
publication = resouce['publication']
urllist = resouce['urllist']
titlepatten = resouce['titlepatten']
keyword = 'meta'


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


for url in urllist:
    html = get_one_page(url)


    selector = Selector(text=html)  # 转换成一个对象
    print(selector)  # 自动添加\<html>\<body>标签
    # //book  选取所有book标签
    liresult=selector.xpath('//li[@class="entry inproceedings"]')
    print(type(liresult))
