# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import os
import smtplib

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = 'fromuser'
password = 'password'
to_addr = 'touser'
smtp_server = 'smtp'

#邮件内容
msg = MIMEMultipart()

msg['From'] = _format_addr('limbo的pc<%s>' % from_addr)
msg['To'] = _format_addr('limbo的iphone<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的图片','utf-8').encode()

#邮件的正文是MIMEText
#msg.attach(MIMEText('hi','html','utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))
#添加附件就是加上一个MIMEBase，从本地读取一个图片

fileindex=os.listdir('/home/limbo/code/py/download')
filestr='/home/limbo/code/py/download/'
with open(filestr+fileindex[0],'rb') as f:
    #这里附件的MIME和文件名
    mime = MIMEBase('image','jpg',filename=fileindex[0])
    #加上必要的头信息
    mime.add_header('Content-Disposition','attachment',filename=fileindex[0])
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    #把附件的内容读进来
    mime.set_payload(f.read())
    #用Base64编码
    encoders.encode_base64(mime)
    msg.attach(mime)
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
