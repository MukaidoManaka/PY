import requests

def requestURL(u,csid,company): # +
    #http://ygapi.gzxjym.com/drp/index/index?u=jiatu&content={"csid":5,"filter":"a.OWNER_NAME = '贵州瓜子物流有限公司'"}   
    _url = "http://ygapi.gzxjym.com/drp/index/index?u=" + u +'&content={"csid":' + str(csid) +',"filter":"a.OWNER_NAME = \'' + company + "'\"}" #少空格或者单双引号不一致均会报错
    return _url

# url = requestURL('jiatu',5,'贵州瓜子物流有限公司')
# res = requests.get(url).text
# print(res)

def requestURL2(u,csid,company): # %
    _url = 'http://ygapi.gzxjym.com/drp/index/index?u=%s&content={"csid":%s,"filter":"a.OWNER_NAME = \'%s\'"}' % (u,csid,company)
    return _url

# url_2 = requestURL2('jiatu',5,'贵州瓜子物流有限公司')
# res = requests.get(url_2).text
# print(res)

def requestURL3(u,csid,company): # format
    _url = 'http://ygapi.gzxjym.com/drp/index/index?u={2}&content={{"csid":{0},"filter":"a.OWNER_NAME = \'{1}\'"}}'.format(csid,company,u)
    return _url

# url_3 = requestURL3('jiatu',5,'贵州瓜子物流有限公司')
# res = requests.get(url_3).text
# print(res)

def requestURL4(u,csid,company): # join ’+’号连接n个字符串需要申请n-1次内存,使用join()需要申请1次内存
    temp = ['http://ygapi.gzxjym.com/drp/index/index?u=',u,'&content={"csid":',str(csid),',"filter":"a.OWNER_NAME = ','\'',company,'\'"}']
    _url = ''.join(temp)
    return _url

url_4 = requestURL4('jiatu',5,'贵州瓜子物流有限公司')
res = requests.get(url_4).text
print(res)