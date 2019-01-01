from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.header import Header
import smtplib


def send_email(content):
    msg = MIMEText('hello', 'plain', 'utf-8')

    # 输入Email地址和口令:
    from_addr = '597561694@qq.com'
    password = ''
    # 输入收件人地址:
    to_addr = '2394346798@qq.com'
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.qq.com'

    msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('来自SMTP的问候....', 'utf-8').encode()

    server = smtplib.SMTP()
    server.set_debuglevel(1)
    server.connect(smtp_server)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


send_email('')