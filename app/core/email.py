import smtplib
from email.mime.text import MIMEText
from email.header import Header
from .config import email_sender,email_server,email_port,email_code

def sendemail(receiver:str,title:str,content:str):
	message = MIMEText(content, 'plain', 'utf-8')
	message['From'] = Header(email_sender)
	message['To'] = Header(receiver)
	message['Subject'] = Header(title, 'utf-8')
	try:
		smtp = smtplib.SMTP(email_server,email_port)
		smtp.connect(email_server,email_port)
		smtp.ehlo()
		smtp.starttls()
		smtp.login(email_sender, email_code)
		smtp.sendmail(email_sender, receiver, message.as_string())
		print('邮件发送成功！')
	except Exception as e:
		print(f'邮件发送失败：{e}')
	finally:
		smtp.quit()
