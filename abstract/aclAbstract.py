import requests
from requests.exceptions import RequestException
import codecs
import re
import time

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

# # 文章列表
# savefile_title='paperlist_acl2019.txt'
# url='https://dblp.org/db/conf/acl/acl2019-1'
# titlepatten= '<span class="title" itemprop="name">(.*?).</span> '
# file=codecs.open(savefile_title, 'w', 'utf-8')
# html = get_one_page(url)
# pattern = re.compile(titlepatten, re.S)
# items = re.findall(pattern, html)
# idd=0
# for item in items:
#     idd=idd+1
#     print(item)
#     file.write(str(idd)+'\t'+item.strip() + '\n')
# file.close()



# #文章下载链接列表
# savefile_title='paperPDFURLlist_acl2019.txt'
# url='https://dblp.org/db/conf/acl/acl2019-1'
# titlepatten= '<li class="ee"><a href="(https://www.aclweb.org/anthology/.*?)" itemprop="url">'
# file=codecs.open(savefile_title, 'w', 'utf-8')
# html = get_one_page(url)
# pattern = re.compile(titlepatten, re.S)
# items = re.findall(pattern, html)
# idd=0
# for item in items:
#     idd=idd+1
#     print(item)
#     file.write(str(idd)+'\t'+item.strip() + '\n')
# file.close()


#文章详情页，下载摘要
readfile='paperPDFURLlist_acl2019.txt'
savefile_abstract='abstract_acl2019.txt'
titlepatten='.pdf>(.*?)</a></h2>'
abstractpatten='abstract = "(.*?)",'

fo = open(readfile, "r")
file = codecs.open(savefile_abstract, 'w', 'utf-8')
idd=0
for line in fo.readlines():  # 依次读取每行
    idd=idd+1
    if(idd<640):
        continue
    time.sleep(2)
    url = line.split('\t')[1].strip()
    print(str(idd)+' '+url)
    html = get_one_page(url)
    # print(html)

    pattern = re.compile(titlepatten, re.S)
    items = re.findall(pattern, html)
    title=items[0].strip()
    # print(str(idd)+' '+title)

    pattern = re.compile(abstractpatten, re.S)
    items = re.findall(pattern, html)
    abstract = items[0].strip()
    # print(abstract)

    file.write(str(idd) + '\t' + title + '\n' + '\t' + abstract + '\n\n')
fo.close()
file.close()
