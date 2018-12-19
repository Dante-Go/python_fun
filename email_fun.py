from email.mime.text import MIMEText
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart('alternative')

html_content = """
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

msg_html = MIMEText(html_content, 'html', 'utf-8')
msg.attach(msg_html)

msg_text = MIMEText('email with header', 'plain', 'utf-8')
msg.attach(msg_text)

header_from = Header('hander_from<xxxxx@qq.com>', 'utf-8')
msg['From'] = header_from

header_to = Header('header_to<xxxxxx@qq.com>', 'utf-8')
msg['To'] = header_to

header_sub = Header('header subject', 'utf-8')
msg['Subject'] = header_sub

from_addr = "2528448730@qq.com"
from_token = "hgcmklipwrxvjfea"

to_addr = "2528448730@qq.com"

smtp_srv = "smtp.qq.com"

try:
	#srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465) # smtp port: 25

	srv = smtplib.SMTP(smtp_srv.encode(), 25)
	srv.starttls()

	srv.set_debuglevel(1)

	srv.login(from_addr, from_token)
	srv.sendmail(from_addr, [to_addr], msg.as_string())
	srv.quit()
except Exception as e:
	print(e)
