#-*- encoding: utf-8 -*-  
import sys  
import locale  
import poplib  
from email import parser  
import email  
import string  
import os
import time
# 确定运行环境的encoding  
__g_codeset = sys.getdefaultencoding()  
if "ascii"==__g_codeset:  
    __g_codeset = locale.getdefaultlocale()[1]  
#  
  
def object2double(obj):  
    if(obj==None or obj==""):  
        return 0  
    else:  
        return float(obj)  
    #end if      
#  
  
def utf8_to_mbs(s):  
    return s.decode("utf-8").encode(__g_codeset)  
#  
  
def mbs_to_utf8(s):  
    return s.decode(__g_codeset).encode("utf-8")  
#  
host = 'host'  
username = 'username'  
password = 'password'  
  
pop_conn = poplib.POP3_SSL(host)  
pop_conn.user(username)  
pop_conn.pass_(password)  
  
#Get messages from server:  
# 获得邮件  
#print('Messages: %s. Size: %s' % pop_conn.stat())
while(True):
	host = 'host'  
	username = 'username'  
	password = 'password'    
  
	pop_conn = poplib.POP3_SSL(host)  
	pop_conn.user(username)  
	pop_conn.pass_(password)  
	test=pop_conn.stat()
	if test[0]==0:
		print('Noemail')
		pop_conn.quit()
		continue
	else:
		print('hahah emailiscoming')
		break

if test[0]==0:
    print ('False')
    pop_conn.quit()
    execfile(r'/home/limbo/code/py/recv.py')
else:
    messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
    messages = ["\n".join(mssg[1]) for mssg in messages]

    messages = [parser.Parser().parsestr(mssg) for mssg in messages]
    i = 0
    for index in range(0,len(messages)):
        message = messages[index];
        i = i + 1;
        subject = message.get('subject')
        h = email.Header.Header(subject)
        dh = email.Header.decode_header(h)
        subject = unicode(dh[0][0], dh[0][1]).encode('utf8')
        mailName = "mail%d.%s" % (i, subject)
        f = open('%d.log'%(i), 'w');
        print >> f, "Date: ", message["Date"]
        print >> f, "From: ", email.utils.parseaddr(message.get('from'))[1]
        print >> f, "To: ", email.utils.parseaddr(message.get('to'))[1]
        print >> f, "Subject: ", subject
        print >> f, "Data: "
        j = 0
        for part in message.walk():
            j = j + 1
            fileName = part.get_filename()
            contentType = part.get_content_type()
            mycode=part.get_content_charset();
            if fileName:
                data = part.get_payload(decode=True)
                h = email.Header.Header(fileName)
                dh = email.Header.decode_header(h)
                fname = dh[0][0]
                encodeStr = dh[0][1]
                if encodeStr != None:
                    fname = fname.decode(encodeStr, mycode)
                fEx = open("%s"%(fname), 'wb')
                fEx.write(data)
                fEx.close()
            elif contentType == 'text/plain':# or contentType == 'text/html':

                data = part.get_payload(decode=True)
                content=str(data);
                if mycode=='gb2312':
                    content= mbs_to_utf8(content)

                nPos = content.find('降息')
                print("nPos is %d"%(nPos))
                print >> f, data
        f.close()

    pop_conn.quit()
list=os.listdir('/home/limbo/code/py/')
sss='1.log'
if sss in list:
	print('here u r')
	
