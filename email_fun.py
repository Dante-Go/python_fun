from email.mime.text import MIMEText
import smtplib

mail_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
        <h1> 这是一封HTML格式邮件</h1>
        </body>
        </html>
        """

msg = MIMEText(mail_content, "html", "utf-8")

from_addr = "2528448730@qq.com"
from_token = "hgcmklipwrxvjfea"

to_addr = "2528448730@qq.com"

smtp_srv = "smtp.qq.com"

try:
	srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465) # smtp port: 25
	srv.login(from_addr, from_token)
	srv.sendmail(from_addr, [to_addr], msg.as_string())
	srv.quit()
except Exception as e:
	print(e)
