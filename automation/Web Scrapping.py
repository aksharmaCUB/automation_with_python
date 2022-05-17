#Web Scrapping
from logging import PlaceHolder
import requests # http requests

from bs4 import BeautifulSoup #web scrapping

import smtplib #send the email
# email body 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime

now = datetime.datetime.now()
# email content placeHolder 
content = ''

# extracting news stories 
def extract_news(url):
    print("Extracting News Stories..")
    cnt=''
    cnt +=('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'\n<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'page_title'})):
        cnt += ((tag.text+'\n'+'<br>') if tag.text!='more' else '')
        # print(cnt)
        # find_all('span',attrs={'class':'sitestr'})
    return(cnt)

cnt = extract_news('https://timesofindia.indiatimes.com/india/timestopten.cms')
content += cnt
content += ('<br>---------<br>')
content += ('<br><br>End of Message')

# lets send the mail 

print('composing Email...')


# make sure to update the Google Low App Access settings before
SERVER = 'smtp.gmail.com' #your smtp server
PORT = 587   # your port number
FROM = ''   # from email id
TO = '' # to email id can be a list
PASS = '' # from email id's password


# fp = open("C:\Users\Ankush Sharma\OneDrive - Cubastion Consulting Pvt Ltd\Desktop\automation\automation\filename.txt","")

msg = MIMEText('')
msg = MIMEMultipart()


# msg.add_header('cintent-Disposition','attachment',filename='empty.txt')
msg['subject'] = 'Top News Stories Times'+' '+str(now.day)+'-'+str(now.month)+'-'+str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content,'html'))

print('Initiating Server....')

server = smtplib.SMTP(SERVER,PORT)

server.set_debuglevel(1)
server.ehlo()
server.starttls()

server.login(FROM,PASS)

server.sendmail(FROM,TO,msg.as_string())

print('Email Sent.....')

server.quit()