import smtplib
from logging_ import BotLogger

from email.mime.text import MIMEText

logger = BotLogger("bot.log")


def send_email_notification(subject, message, user_info={}):

    smtp_server = "smtp.gmail.com"
    smtp_port = 465
    smtp_username = "zoo_bot"
    smtp_password = "password"

    sender = "ivfmn1@gmail.com"
    recipient = "ivfmn1@gmail.com"
    message_full = f"Результаты викторины: {message}\n\nДанные пользователя:\nid: {user_info['id_']}\nFirst name: {user_info['first_name']}\nUsername: {user_info['username']}\nLast name: {user_info['last_name']}\nLanguage: {user_info['language_code']}"
    msg = MIMEText(message_full)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    try:
        with smtplib.SMTP(smtp_server, smtp_port, timeout=20.0) as server:
            print("server context")
            server.login(smtp_username, smtp_password)
            print("logged in")
            server.sendmail(sender, recipient, msg.as_string())
            print("sent")
    except Exception as e:
        print(e)
        logger.log(
            "error", f"Error occured when trying to send email notification: {e}"
        )
