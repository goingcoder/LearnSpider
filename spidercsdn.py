#! usr/bin/env python
# _*_ coding:utf-8 _*_
#导入要使用的模块
import urllib, urllib2, cookielib
from bs4 import BeautifulSoup

#创建cookie对象
cookie = cookielib.CookieJar()
#创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
#创建opener对象
opener = urllib2.build_opener(handler)
url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
#获取登录页面，捕获异常
try:
    response = opener.open(url)
except urllib2.URLError as e:
    if hasattr(e,'reason'):
        print 'We failed to reach a server.'
        print 'Reason:',e.reason
    elif hasattr(e,'code'):
        print "The server couldn't fulfill the request."
        print 'Error code:',e.code
#将获取的页面传给BeautifulSoup构造BeautifulSoup对象
soup = BeautifulSoup(response.read(),'lxml')
#根据标签和属性获得input标签
inputs = soup.find_all('input', attrs={'type':'hidden'})
#根据属性获得值
lt = inputs[0]['value']
execution=inputs[1]['value']
#前面页面获取成功，说明服务器没有检测头部
username = ''
password = ''
values={'username':username, 'password':password, 'lt':lt, 'execution':execution, '_eventId':'submit'}
#把数据编程特定格式
datas=urllib.urlencode(values)
AccpetLanguage='zh-CN,zh;q=0.8'
referer = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'
headers = {'User-Agent':userAgent, 'Accept-Language':AccpetLanguage, 'Referer':referer}
request = urllib2.Request(url, datas, headers)
try:
    res = opener.open(request)
except urllib2.URLError as e:
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason:', e.reason
    elif hasattr(e, 'code'):
        print "The server couldn't fulfill the request."
        print 'Error code:', e.code
print "Response's info:", res.info()
#判断对象是否为空
print any(res)
new_url = 'http://my.csdn.net'
#不加headers，会保403拒绝访问
req = urllib2.Request(new_url,datas, headers=headers)
#获取登录后的页面，可以看到自己的用户名等等信息
r = opener.open(req)
print r.read()
