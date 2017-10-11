#!/usr/bin/env python3
# coding: utf-8
import smtplib
from email.mime.text import MIMEText
import configparser

def send_email(myaddr):
    info = get_email_config()
    sender = info['sender']
    receiver = info['receiver']
    subject =  info['subject']
    smtpserver = info['smtpserver']
    username = info['username']
    password = info['password']

    msg = MIMEText(myaddr, 'html', 'utf-8')  # 中文需参数‘utf-8’，单字节字符不需要
    msg['Subject'] = subject

    smtp = smtplib.SMTP_SSL(smtpserver,465)
    smtp.connect('smtp.qq.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()



def get_email_config():
    config=configparser.ConfigParser()
    config.read('config.ini')
    info = {}
    info['sender'] = config.get("email","sender")
    info['receiver'] = config.get("email","receiver")
    info['subject'] = config.get("email","subject")
    info['smtpserver'] = config.get("email","smtpserver")
    info['username'] = config.get("email","username")
    info['password'] = config.get("email","password")
    return info

import socket

def get_ip():
    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)
    return myaddr