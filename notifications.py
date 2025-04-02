import smtplib
from logging_ import BotLogger

from email.mime.text import MIMEText

logger = BotLogger("bot.log")


def send_email_notification(subject, message):
    smtp_server = "imap.yandex.com"
    smtp_port = 465
    smtp_username = "my_zoo_bot"
    smtp_password = "trhjggtavcetwszj"

    sender = "ivfmn1@yandex.ru"
    recipient = "ivfmn1@yandex.ru"

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.login(smtp_username, smtp_password)
            server.sendmail(sender, recipient, msg.as_string())
    except Exception as e:
        logger.log("error", f"Ошибка при отправлении уведомления по почте: {e}")


# TODO test
