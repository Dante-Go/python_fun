import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Hello, email demo", "plain", "utf-8")

from_addr = "2528448730@qq.com"
from_token = "xxxxxxxxxxxxxxx"

to_addr = "2528448730@qq.com"

smtp_srv = "smtp.qq.com"

try:
	srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465) # smtp port: 25
	srv.login(from_addr, from_token)
	srv.sendmail(from_addr, [to_addr], msg.as_string())
	srv.quit()
except Exception as e:
	print(e)
