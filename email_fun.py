from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEBase, MIMEMultipart

mail_mul = MIMEMultipart()

mail_text = MIMEText('email with attachment', 'plain', 'utf-8')

mail_mul.attach(mail_text)

with open('hano.py', 'rb') as f:
	s = f.read()
	m = MIMEText(s, 'base64', 'utf-8')
	m['Content-Type'] = 'application/octet-stream'
	m['Content-Disposition'] = 'attachment; filename="hano.py"'
	mail_mul.attach(m)

from_addr = "2528448730@qq.com"
from_token = "hgcmklipwrxvjfea"

to_addr = "2528448730@qq.com"

smtp_srv = "smtp.qq.com"

try:
	srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465) # smtp port: 25
	srv.login(from_addr, from_token)
	srv.sendmail(from_addr, [to_addr], mail_mul.as_string())
	srv.quit()
except Exception as e:
	print(e)
