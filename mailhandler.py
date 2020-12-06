import pymongo
from pymongo import MongoClient
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

import json


class Mailhandler():

    def __init__(self):
        self.client=MongoClient('localhost', 27017)
        self.db=self.client.alumni
    

    def send_mail_alumni(self):
        send_alumni=[]
        for d in self.db.alumnies.distinct('alumni_email'):
                 send_alumni.append(d)

        print(send_alumni) 
   

        for i in send_alumni:
                    TO = i
                    FROM ='sspathak@mitaoe.ac.in'
                    BODY = """
                        <head><META http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body>
                    
                    
                    
                    
                    <div style="background-color:#f4f4f5">
                    <table cellpadding="0" cellspacing="0" style="width:100%;height:100%;background-color:#f4f4f5;text-align:center">
                    <tbody><tr>
                    <td style="text-align:center">
                    <table align="center" cellpadding="0" cellspacing="0" style="background-color:#fff;width:100%;max-width:680px;height:100%">
                    <tbody><tr>
                    <td>
                    <table align="center" cellpadding="0" cellspacing="0" style="text-align:left;padding-bottom:88px;width:100%;padding-left:120px;padding-right:120px">
                    <tbody>
                    <tr>
                    <td colspan="2" style="padding-top:72px;color:#000000;font-family:&#39;Postmates Std&#39;,&#39;Helvetica&#39;,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif;font-size:48px;font-style:normal;font-weight:600;letter-spacing:-2.6px;line-height:52px;text-decoration:none"><center><img src="http://Capture.PNG" alt="" height="100px"></center></td>
                    </tr>
                    <tr>
                    <td style="padding-top:48px;padding-bottom:48px">
                    <table cellpadding="0" cellspacing="0" style="width:100%">
                    <tbody><tr>
                    <td style="width:100%;height:1px;max-height:1px;background-color:#d9dbe0"></td>
                    </tr>
                    </tbody></table>
                    </td>
                    </tr>
                    <tr>
                    <td style="color:#9095a2;font-family:&#39;Postmates Std&#39;,&#39;Helvetica&#39;,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif;font-size:16px;font-style:normal;font-weight:400;letter-spacing:-0.18px;line-height:24px;text-decoration:none;vertical-align:top;width:100%">
                    <b>Hii, Kedar Paresewar</b>  <br><br>                                  
                    Woww! Thanks for Creating Account in Class Reunion! We are Welcome Here and follow below Instruction 
                                                        </td>
                    </tr>
                    <tr>
                    <td style="padding-top:24px;color:#9095a2;font-family:&#39;Postmates Std&#39;,&#39;Helvetica&#39;,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif;font-size:16px;font-style:normal;font-weight:400;letter-spacing:-0.18px;line-height:24px;text-decoration:none;vertical-align:top;width:100%">
                                                        Please tap the button below to Confirm your Account.
                                                        </td>
                    </tr>
                    <tr>
                    <td>
                    <a  href="http://localhost:5000/sign" style="margin-top:36px;color:#ffffff;font-family:&#39;Postmates Std&#39;,&#39;Helvetica&#39;,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif;font-size:12px;font-style:normal;font-weight:600;letter-spacing:0.7px;line-height:48px;text-decoration:none;vertical-align:top;width:220px;background-color:#00cc99;border-radius:28px;display:block;text-align:center;text-transform:uppercase">
                                                            Confirm Account
                                                        </a>
                    
                    </td>
                    </tr>
                    </tbody></table>
                    </td>
                    </tr>
                    </tbody></table>
                
                    </td></tr></tbody></table></div></body>
                
                
                    """
                    SUBJECT="Class Reunion"
            
                    """With this function we send out our html email"""
                
                    # Create message container - the correct MIME type is multipart/alternative here!
                    MESSAGE = MIMEMultipart('alternative')
                    MESSAGE['subject'] = SUBJECT
                    MESSAGE['To'] = TO
                    MESSAGE['From'] = FROM
                    # Record the MIME type text/html.
                    HTML_BODY = MIMEText(BODY, 'html')
                
                    # Attach parts into message container.
                    # According to RFC 2046, the last part of a multipart message, in this case
                    # the HTML message, is best and preferred.
                    MESSAGE.attach(HTML_BODY)
                
                    # The actual sending of the e-mail
                    server = smtplib.SMTP('smtp.gmail.com:587')
                
                    # Print debugging output when testing
                    server.set_debuglevel(1)
                
                    # Credentials (if needed) for sending the mail
                    password = "Sarvesh@5734"
                
                    server.starttls()
                    server.login(FROM,password)
                    server.sendmail(FROM, [TO], MESSAGE.as_string())
                    server.quit()
                



    def send_message_alumni(self,event_details):
        send_alumni=[]
        for d in self.db.alumnies.distinct('alumni_phone'):
                 send_alumni.append(d)


        
        URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
        def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
            req_params = {
            'apikey':apiKey,
            'secret':secretKey,
            'usetype':useType,
            'phone': phoneNo,
            'message':textMessage,
            'senderid':senderId
            }
            return requests.post(reqUrl, req_params)

        # get response
        for i in send_alumni:
            response = sendPostRequest(URL, 'EVW6OMRWGGTT7HDLZM19ORGL1UGCHQB7', 'KOXTHZQXE9JNQBFN', 'stage', i, 'patilpavan631@gmail.com',  event_details['event_description'])
        """
        Note:-
            you must provide apikey, secretkey, usetype, mobile, senderid and message values
            and then requst to api
        """
        # print response if you want
        print (response.text)
        print(send_alumni)

    def send_message(self,data):    
        message=data['message']

        mobile=data['phone']
        print(mobile)
        print(message)
        


        
        URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
        def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
            req_params = {
            'apikey':apiKey,
            'secret':secretKey,
            'usetype':useType,
            'phone': phoneNo,
            'message':textMessage,
            'senderid':senderId
            }
            return requests.post(reqUrl, req_params)

        response = sendPostRequest(URL, 'EVW6OMRWGGTT7HDLZM19ORGL1UGCHQB7', 'KOXTHZQXE9JNQBFN', 'stage', mobile, 'patilpavan631@gmail.com', message )
        
        print (response.text)
       




    def send_mail_event_details(self,data):
        send_alumni=[]
        for d in self.db.alumnies.distinct('alumni_email'):
                 send_alumni.append(d)

        print(send_alumni) 

   

        for i in send_alumni:
                    TO = i
                    FROM ='sspathak@mitaoe.ac.in'
                    # BODY = data['event_description']
                    
                    BODY = """
                        <head><META http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body>
                    
                    
                    
                    
                    <div style="background-color:#f4f4f5">
                    <table cellpadding="0" cellspacing="0" style="width:100%;height:100%;background-color:#f4f4f5;text-align:center">
                    <tbody><tr>
                    <td style="text-align:center">
                    <table align="center" cellpadding="0" cellspacing="0" style="background-color:#fff;width:100%;max-width:680px;height:100%">
                    <tbody><tr>
                    <td>
                    <table align="center" cellpadding="0" cellspacing="0" style="text-align:left;padding-bottom:88px;width:100%;padding-left:120px;padding-right:120px">
                    <tbody>
                    <tr>
                    <td colspan="2" style="padding-top:72px;color:#000000;font-family:&#39;Postmates Std&#39;,&#39;Helvetica&#39;,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif;font-size:48px;font-style:normal;font-weight:600;letter-spacing:-2.6px;line-height:52px;text-decoration:none"><center><img src="http://Capture.PNG" alt="" height="100px"></center></td>
                    </tr>
                    <tr>
                    <td style="padding-top:48px;padding-bottom:48px">
                    <table cellpadding="0" cellspacing="0" style="width:100%">
                    <tbody><tr>
                    <td style="width:100%;height:1px;max-height:1px;background-color:#d9dbe0"></td>
                    </tr>
                    </tbody></table>
                    </td>
                    </tr>
                    <tr>
                    <td style="color:#9095a2;font-family:&#39;Postmates Std&#39;,&#39;Helvetica&#39;,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif;font-size:16px;font-style:normal;font-weight:400;letter-spacing:-0.18px;line-height:24px;text-decoration:none;vertical-align:top;width:100%">
                    <b>Hii, """+i[0]+""" Greetings From MITAOE .We are organising """+data['event_title']+"""</b>  <br><br>                                  
                      """+data['event_description']+"""
                    
                    
                                                        </td>
                    </tr>
                    
                    
                    </tr>
                    </tbody></table>
                    </td>
                    </tr>
                    </tbody></table>
                
                    </td></tr></tbody></table></div></body>
                
                
                    """

                  
                    SUBJECT=data['event_title']
            
                    """With this function we send out our html email"""
                
                    # Create message container - the correct MIME type is multipart/alternative here!
                    MESSAGE = MIMEMultipart('alternative')
                    MESSAGE['subject'] = SUBJECT
                    MESSAGE['To'] = TO
                    MESSAGE['From'] = FROM
                    # Record the MIME type text/html.
                    HTML_BODY = MIMEText(BODY, 'html')
                
                    # Attach parts into message container.
                    # According to RFC 2046, the last part of a multipart message, in this case
                    # the HTML message, is best and preferred.
                    MESSAGE.attach(HTML_BODY)
                
                    # The actual sending of the e-mail
                    server = smtplib.SMTP('smtp.gmail.com:587')
                
                    # Print debugging output when testing
                    server.set_debuglevel(1)
                
                    # Credentials (if needed) for sending the mail
                    password = "Sarvesh@5734"
                
                    server.starttls()
                    server.login(FROM,password)
                    server.sendmail(FROM, [TO], MESSAGE.as_string())
                    server.quit()
    
    def send_mail_fundraising_details(self,data):
        send_alumni=[]
        for d in self.db.alumnies.distinct('alumni_email'):
                 send_alumni.append(d)

        print(send_alumni) 

   

        for i in send_alumni:
                    TO = i
                    FROM ='ksparsewar1023@gmail.com'
                    # BODY = data['event_description']
                    
                    BODY = """
                        <head><META http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body>
                    
                    
                    
                    
                    <div style="background-color:#f4f4f5">
                    <table cellpadding="0" cellspacing="0" style="width:100%;height:100%;background-color:#f4f4f5;text-align:center">
                    <tbody><tr>
                    <td style="text-align:center">
                    <table align="center" cellpadding="0" cellspacing="0" style="background-color:#fff;width:100%;max-width:680px;height:100%">
                    <tbody><tr>
                    <td>
                    <table align="center" cellpadding="0" cellspacing="0" style="text-align:left;padding-bottom:88px;width:100%;padding-left:120px;padding-right:120px">
                    <tbody>
                    <tr>
                    <td colspan="2" style="padding-top:72px;color:#000000;font-family:&#39;Postmates Std&#39;,&#39;Helvetica&#39;,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif;font-size:48px;font-style:normal;font-weight:600;letter-spacing:-2.6px;line-height:52px;text-decoration:none"><center><img src="http://Capture.PNG" alt="" height="100px"></center></td>
                    </tr>
                    <tr>
                    <td style="padding-top:48px;padding-bottom:48px">
                    <table cellpadding="0" cellspacing="0" style="width:100%">
                    <tbody><tr>
                    <td style="width:100%;height:1px;max-height:1px;background-color:#d9dbe0"></td>
                    </tr>
                    </tbody></table>
                    </td>
                    </tr>
                    <tr>
                    <td style="color:#9095a2;font-family:&#39;Postmates Std&#39;,&#39;Helvetica&#39;,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif;font-size:16px;font-style:normal;font-weight:400;letter-spacing:-0.18px;line-height:24px;text-decoration:none;vertical-align:top;width:100%">
                    <b>Hii, """+i[0]+""" Greetings From MITAOE .We are organising """+data['event_title']+"""</b>  <br><br>                                  
                      """+data['event_description']+"""
                    
                    
                                                        </td>
                    </tr>
                    
                    
                    </tr>
                    </tbody></table>
                    </td>
                    </tr>
                    </tbody></table>
                
                    </td></tr></tbody></table></div></body>
                
                
                    """

                  
                    SUBJECT=data['event_title']
            
                    """With this function we send out our html email"""
                
                    # Create message container - the correct MIME type is multipart/alternative here!
                    MESSAGE = MIMEMultipart('alternative')
                    MESSAGE['subject'] = SUBJECT
                    MESSAGE['To'] = TO
                    MESSAGE['From'] = FROM
                    # Record the MIME type text/html.
                    HTML_BODY = MIMEText(BODY, 'html')
                
                    # Attach parts into message container.
                    # According to RFC 2046, the last part of a multipart message, in this case
                    # the HTML message, is best and preferred.
                    MESSAGE.attach(HTML_BODY)
                
                    # The actual sending of the e-mail
                    server = smtplib.SMTP('smtp.gmail.com:587')
                
                    # Print debugging output when testing
                    server.set_debuglevel(1)
                
                    # Credentials (if needed) for sending the mail
                    password = "kedar1023"
                
                    server.starttls()
                    server.login(FROM,password)
                    server.sendmail(FROM, [TO], MESSAGE.as_string())
                    server.quit()
            
    def sendmailmodule(self,data):
        
                    TO = data['mail']
                    FROM ='ksparsewar1023@gmail.com'
                    BODY = """
                        <head><META http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body>
                    
                    
                    
                    
                    <div style="background-color:#f4f4f5">
                    <table cellpadding="0" cellspacing="0" style="width:100%;height:100%;background-color:#f4f4f5;text-align:center">
                    <tbody><tr>
                    <td style="text-align:center">
                    <table align="center" cellpadding="0" cellspacing="0" style="background-color:#fff;width:100%;max-width:680px;height:100%">
                    <tbody><tr>
                    <td>
                    <table align="center" cellpadding="0" cellspacing="0" style="text-align:left;padding-bottom:88px;width:100%;padding-left:120px;padding-right:120px">
                    <tbody>
                    <tr>
                    <td colspan="2" style="padding-top:72px;color:#000000;font-family:&#39;Postmates Std&#39;,&#39;Helvetica&#39;,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif;font-size:48px;font-style:normal;font-weight:600;letter-spacing:-2.6px;line-height:52px;text-decoration:none"><center><img src="http://Capture.PNG" alt="" height="100px"></center></td>
                    </tr>
                    <tr>
                    <td style="padding-top:48px;padding-bottom:48px">
                    <table cellpadding="0" cellspacing="0" style="width:100%">
                    <tbody><tr>
                    <td style="width:100%;height:1px;max-height:1px;background-color:#d9dbe0"></td>
                    </tr>
                    </tbody></table>
                    </td>
                    </tr>
                    <tr>
                    <td style="color:#9095a2;font-family:&#39;Postmates Std&#39;,&#39;Helvetica&#39;,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif;font-size:16px;font-style:normal;font-weight:400;letter-spacing:-0.18px;line-height:24px;text-decoration:none;vertical-align:top;width:100%">
                    <b>"""+data['message']+"""                                 
                                                        </td>
                    </tr>
                    <tr>
                    </tr>
                    <tr>
                    <td>
                    </td>
                    </tr>
                    </tbody></table>
                    </td>
                    </tr>
                    </tbody></table>
                
                    </td></tr></tbody></table></div></body>
                
                
                    """
                    SUBJECT= data['subject']
            
                    """With this function we send out our html email"""
                
                    # Create message container - the correct MIME type is multipart/alternative here!
                    MESSAGE = MIMEMultipart('alternative')
                    MESSAGE['subject'] = SUBJECT
                    MESSAGE['To'] = TO
                    MESSAGE['From'] = FROM
                    # Record the MIME type text/html.
                    HTML_BODY = MIMEText(BODY, 'html')
                
                    # Attach parts into message container.
                    # According to RFC 2046, the last part of a multipart message, in this case
                    # the HTML message, is best and preferred.
                    MESSAGE.attach(HTML_BODY)
                
                    # The actual sending of the e-mail
                    server = smtplib.SMTP('smtp.gmail.com:587')
                
                    # Print debugging output when testing
                    server.set_debuglevel(1)
                
                    # Credentials (if needed) for sending the mail
                    password = "kedar1023"
                
                    server.starttls()
                    server.login(FROM,password)
                    server.sendmail(FROM, [TO], MESSAGE.as_string())
                    server.quit()
    

    def send_mail_notice(self,data):
        send_alumni=[]
        for d in self.db.alumnies.distinct('alumni_email'):
                 send_alumni.append(d)

        print(send_alumni) 

   

        for i in send_alumni:
                    TO = i
                    FROM ='ksparsewar1023@gmail.com'
                    # BODY = data['event_description']
                    
                    BODY = """
                        <head><META http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body>
                    
                    
                    
                    
                    <div style="background-color:#f4f4f5">
                    <table cellpadding="0" cellspacing="0" style="width:100%;height:100%;background-color:#f4f4f5;text-align:center">
                    <tbody><tr>
                    <td style="text-align:center">
                    <table align="center" cellpadding="0" cellspacing="0" style="background-color:#fff;width:100%;max-width:680px;height:100%">
                    <tbody><tr>
                    <td>
                    <table align="center" cellpadding="0" cellspacing="0" style="text-align:left;padding-bottom:88px;width:100%;padding-left:120px;padding-right:120px">
                    <tbody>
                    <tr>
                    <td colspan="2" style="padding-top:72px;color:#000000;font-family:&#39;Postmates Std&#39;,&#39;Helvetica&#39;,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif;font-size:48px;font-style:normal;font-weight:600;letter-spacing:-2.6px;line-height:52px;text-decoration:none"><center><img src="http://Capture.PNG" alt="" height="100px"></center></td>
                    </tr>
                    <tr>
                    <td style="padding-top:48px;padding-bottom:48px">
                    <table cellpadding="0" cellspacing="0" style="width:100%">
                    <tbody><tr>
                    <td style="width:100%;height:1px;max-height:1px;background-color:#d9dbe0"></td>
                    </tr>
                    </tbody></table>
                    </td>
                    </tr>
                    <tr>
                    <td style="color:#9095a2;font-family:&#39;Postmates Std&#39;,&#39;Helvetica&#39;,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif;font-size:16px;font-style:normal;font-weight:400;letter-spacing:-0.18px;line-height:24px;text-decoration:none;vertical-align:top;width:100%">
                    <b>Hii, """+i[0]+""" Greetings From MITAOE . """+data["Message"]+"""                    
                    
                                                        </td>
                    </tr>
                    
                    
                    </tr>
                    </tbody></table>
                    </td>
                    </tr>
                    </tbody></table>
                
                    </td></tr></tbody></table></div></body>
                
                
                    """

                  
                    SUBJECT="IMPORTANT NOTICE"
            
                    """With this function we send out our html email"""
                
                    # Create message container - the correct MIME type is multipart/alternative here!
                    MESSAGE = MIMEMultipart('alternative')
                    MESSAGE['subject'] = SUBJECT
                    MESSAGE['To'] = TO
                    MESSAGE['From'] = FROM
                    # Record the MIME type text/html.
                    HTML_BODY = MIMEText(BODY, 'html')
                
                    # Attach parts into message container.
                    # According to RFC 2046, the last part of a multipart message, in this case
                    # the HTML message, is best and preferred.
                    MESSAGE.attach(HTML_BODY)
                
                    # The actual sending of the e-mail
                    server = smtplib.SMTP('smtp.gmail.com:587')
                
                    # Print debugging output when testing
                    server.set_debuglevel(1)
                
                    # Credentials (if needed) for sending the mail
                    password = "kedar1023"
                
                    server.starttls()
                    server.login(FROM,password)
                    server.sendmail(FROM, [TO], MESSAGE.as_string())
                    server.quit()
    
