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