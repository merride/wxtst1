from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import hashlib
from boto.connection import HTTPResponse
from django.http.response import HttpResponse

@csrf_exempt


def checkSignature(request):
    signature=request.GET.get('signature',None)
    timestamp=request.GET.get('timestamp',None)
    nonce=request.GET.get('nonce',None)
    echostr=request.GET.get('echostr',None)
    token='merride'
    tmplist=[token,timestamp,nonce]
    tmplist.sort()
    tmpstr="%s%s%s"%tuple(tmplist)
    tmpstr=hashlib.sha1(tmpstr).hexdigest()
    if tmpstr==signature:
        return echostr
    else:
        return None


def index(request):
    if request.method=='GET':
        response=HttpResponse(checkSignature(request))
        return response
    else:
        return HttpResponse('Hello World')
    


"""def responseMsg(request):  
    rawStr = smart_str(request.raw_post_data)  
    #rawStr = smart_str(request.POST['XML'])  
    msg = paraseMsgXml(ET.fromstring(rawStr))  
      
    queryStr = msg.get('Content','You have input nothing~')  
  
    '''raw_youdaoURL = "http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%s&type=data&doctype=%s&version=1.1&q=" % (YOUDAO_KEY_FROM,YOUDAO_KEY,YOUDAO_DOC_TYPE)     
    youdaoURL = "%s%s" % (raw_youdaoURL,urllib2.quote(queryStr))  
  
    req = urllib2.Request(url=youdaoURL)  
    result = urllib2.urlopen(req).read()'''  
  
    replyContent = paraseYouDaoXml(ET.fromstring(result))  
  
    return getReplyXml(msg,replyContent)  
"""

Class wxinterface(View)：
    def __init__(self):
        self.TOKEN='merride'
    def post(self,request,*args,**kwargs):
        xml_str=request.body
        xml=ET.fromstring(xml_str)
        content=xml.find('Content').text
        msgType=xml.find('MsgType').text
        fromUserName=xml.find('FromUserName').text
        toUserName=xml.find('ToUserName').text
        createTime=xml.find('CreateTime').text
        reply='''
               <xml>
               <ToUserName>%s</ToUserName>
               <FromUserName>%s</FromUserName>
               <CreateTime>%s</CreateTime>
               <MsgType>%s</MsgType>
               <Content>%s</Content>
               </xml>'''%(fromUserName,toUserName,str(int(time.time())),msgType,content)
        return HttpResponse(reply,content_type="application/xml")
    @csrf_exempt
    def dispatch(self,*args,**kwargs):
        return super(wxinterface,self).dispatch(*args,**kwargs)
               
