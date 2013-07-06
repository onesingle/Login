#coding:utf-8
#by oensingle

import urllib,urllib2,re,cookielib,string
from bs4 import BeautifulSoup
#构造报头
headers = {
#'Host': 'www.ipahuo.com'
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0',
'Accept-Language':'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'Content-Type': 'application/x-www-form-urlencoded'
}
url = 'http://www.ipahuo.com/login.aspx?u=http://www.ipahuo.com/home'
txtpassword='你的密码'
# first HTTP request without form data
cj=cookielib.CookieJar()
cookie_support=urllib2.HTTPCookieProcessor(cj)
opener=urllib2.build_opener(cookie_support,urllib2.HTTPBasicAuthHandler)
urllib2.install_opener(opener)
f = opener.open(url)
print cj._cookies.values()
soup = BeautifulSoup(f)
# parse and retrieve two vital form values
viewstate = soup.select("#__VIEWSTATE")[0]['value']
eventvalidation = soup.select("#__EVENTVALIDATION")[0]['value']
print viewstate
print eventvalidation
#如果post 需要 顺序的话用list
formData = [
    ('__VIEWSTATE',viewstate),
    ('__EVENTVALIDATION',eventvalidation),
    ('txtusername','你的账户'),
    ('txtpassword',txtpassword),
    ('ButLogin','登 录'),
    ]
encodedFields = urllib.urlencode(formData)
print encodedFields
# second HTTP request with form data
result=opener.open(url,encodedFields)
print "网址"
print result.geturl()
text=result.read()
print result.getcode()
print result.info()
#print text
p=re.compile(r'href=\"signout\"')
try:
    # actually we'd better use BeautifulSoup once again to
    # retrieve results(instead of writing out the whole HTML file)
    # Besides, since the result is split into multipages,
    # we need send more HTTP requests
    loginsusse=p.search(text)

    print "登录成功哦"
except:
    print('Could not open output file\n')

qiandao=urllib2.urlopen('http://www.ipahuo.com/depot')
qiandaotext=qiandao.read()

qiandao1=re.compile(r"img src=\"http://disc1.ipahuo.com/user/91/1/635082945281567597_330x330_330.jpg")
qiandao1cg=qiandao1.search(qiandaotext)
if qiandao1cg:
    print "找到了"
else:
    print "么u，找到"
#查找签到链接
soup1= BeautifulSoup(qiandaotext)
tupian=soup1.select(".inimg")
print tupian
pat = re.compile(r'/depot/content/.......')

#pat = re.compile(r'href=\"([^"]*)\"')
jieguo=pat.search(str(tupian))
wenben=jieguo.group(0)
print wenben
print len(wenben)
#shuzi=jieguo[]
print wenben[15:22]
shuzi=string.atol(wenben[15:22])
i=0
while i<=4: 
    haole= 'http://www.ipahuo.com/depot/content/'+str(shuzi)
    shuzi+=1
    print haole
    opener.open(haole)
    print urllib.urlopen(haole).info()
    i+=1 
lingqian="http://www.ipahuo.com//apiuser/UserCheckinGetMoneys/"+'89865'
opener.open(lingqian)
