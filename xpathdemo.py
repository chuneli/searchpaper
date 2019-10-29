html='''
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
<book>
        <title lang="eng1">Harry Potter</title>
        <price>29.99</price>
    <div>
        <book>123456</book>
    </div>
</book>

<book>
  <title lang="eng2">Learning XML</title>
  <price>39.95</price>
</book>
<book>3333333333333333</book>
<book>4444444444444444</book>
</bookstore>
'''

from scrapy.selector import Selector
selector = Selector(text=html)  #转换成一个对象
#print(selector)     #自动添加\<html>\<body>标签

#//book  选取所有book标签
# print(selector.xpath('//book'))
# print(selector.xpath('//@lang'))
# print(selector.xpath('//title[@lang="eng2"]'))   # lang属性等于eng2的title节点
bookstort = selector.xpath('//bookstore')[0]
print(bookstort.xpath('./book[price>35]')) #bookstort中间的book节点的price节点取值大于35的book节点

