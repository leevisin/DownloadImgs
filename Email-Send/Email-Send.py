import smtplib
from email.mime.text import MIMEText
import traceback
import sys


def send_email(subject, message, from_addr, to_addr, smtp_server, smtp_port, smtp_user, smtp_pass):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.sendmail(from_addr, [to_addr], msg.as_string())


def main():
    try:
        # 将要尝试执行的代码
        # 例如: 1/0 # 这将引发除以零的异常

        # 如果没有错误，发送成功邮件
        send_email("程序运行成功",
                   "程序已成功完成执行。",
                   "your-email@example.com", "receiver@example.com",
                   "smtp.example.com", 587, "your-email@example.com", "your-password")

    except Exception as e:
        error_msg = traceback.format_exc()
        # 发生错误时，发送错误邮件
        send_email("程序运行出错",
                   "程序运行时发生以下错误:\n\n" + error_msg,
                   "your-email@example.com", "receiver@example.com",
                   "smtp.example.com", 587, "your-email@example.com", "your-password")
        print(error_msg)
        sys.exit(-1)


if __name__ == "__main__":
    main()
