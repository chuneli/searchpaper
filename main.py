import settings
import requests
import codecs
from requests.exceptions import RequestException
import re

# keyword = 'meta'
# keyword = 'transfer'
# keyword = 'compress'
keyword = 'shot'
download = False


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


def do_one_job(keyword,publication,urllist,titlepatten):
    outfile = 'results/'+keyword +'_'+publication+'.txt'
    number = 0
    file=codecs.open(outfile, 'w', 'utf-8')
    for url in urllist:
        html = get_one_page(url)
        #print(html)
        pattern = re.compile(titlepatten, re.S)
        items = re.findall(pattern, html)
        for item in items:
            if item.lower().find(keyword.lower()) > -1:
                file.write(item.strip()+'\n')
                number=number+1
        file.write('\n')
    file.close()
    print(keyword +'_'+publication+" : "+str(number))
    return number

results={}
for resouce in settings.resources:
    publication=resouce['publication']
    urllist=resouce['urllist']
    titlepatten=resouce['titlepatten']
    number=do_one_job(keyword, publication, urllist, titlepatten)
    results[publication]=number


################  statistic ###################
publications=results.keys()
yearset,confset=set(),set()
for publication in publications:
    frags=publication.split(' ')
    confset.add(frags[0])
    yearset.add(frags[1])

yearlist=list(yearset)
yearlist.sort()
conflist=list(confset)
conflist.sort()
yeartotal={}
for year in yearlist:
    yeartotal[year]=0

print('    ',end='\t')
for year in yearlist:
    print(year,end='\t')
print('total')


for conf in conflist:
    print(conf,end='\t')
    confsum=0
    for year in yearlist:
        key=conf+' '+year
        if( results.get(key)):
            print(results[key],end='   \t')
            confsum=confsum+results[key]
            yeartotal[year]=yeartotal[year]+results[key]
        else:
            print(' ', end='   \t')
    print(confsum)

allsum=0
print('total',end='\t')
for year in yearlist:
    print(yeartotal[year],end='   \t')
    allsum=allsum+yeartotal[year]
print( allsum)