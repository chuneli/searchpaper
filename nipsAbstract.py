import requests
from requests.exceptions import RequestException
import codecs
import re

url='https://papers.nips.cc/book/advances-in-neural-information-processing-systems-32-2019'
# inputfile='nips2019.html'
savefile_title='paperlist_nips2019.txt'
savefile_abstract='abstract_nips2019.txt'

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


# titlepatten='<li><a href="/paper/(.*?)">(.*?)</a> <a href="/author/'
# file=codecs.open(savefile_title, 'w', 'utf-8')
# html = get_one_page(url)
# pattern = re.compile(titlepatten, re.S)
# items = re.findall(pattern, html)
# idd=0
# for item in items:
#     idd=idd+1
#     print(item[1])
#     file.write(str(idd)+'\t'+item[1].strip() + '\n')
# file.close()

titlepatten='<li><a href="(/paper/.*?)">(.*?)</a> <a href="/author/'
abstractpatten='<p class="abstract">(.*?)</p>'
file=codecs.open(savefile_abstract, 'w', 'utf-8')

html = get_one_page(url)
pattern = re.compile(titlepatten, re.S)
items = re.findall(pattern, html)
idd=0
for item in items:
    idd=idd+1
    if idd<=390:
        continue
    abstracturl='https://papers.nips.cc'+item[0]
    title=item[1].strip()
    print(idd, title)
    abstracthtml = get_one_page(abstracturl)
    pattern = re.compile(abstractpatten, re.S)
    try:
        abstract=re.findall(pattern, abstracthtml)[0].strip()
    except RequestException:
        abstract=''
    file.write(str(idd)+'\t'+title+ '\n'+'\t'+abstract+'\n\n')
file.close()
