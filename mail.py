'''
Program to send mail from GMAIL using SMTP
'''
import smtplib

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
GMAIL_USERNAME = 'ksparsewar1023@gmail.com'
GMAIL_PASSWORD = 'kedar1023' #CAUTION: This is stored in plain text!

recipient = 'sspathak@gmail.com'
subject = 'Test SIH 2020'
emailText = 'SIH2020'

emailText = "" + emailText + ""

headers = ["From: " + GMAIL_USERNAME,
           "Subject: " + subject,
           "To: " + recipient,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers = "\r\n".join(headers)

session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

session.ehlo()
session.starttls()
session.ehlo

session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + emailText)

session.quit()

