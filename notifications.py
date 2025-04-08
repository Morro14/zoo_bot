import smtplib
from logging_ import BotLogger
from env import smtp_password, smtp_port, smtp_server, smtp_username
from email.mime.text import MIMEText

logger = BotLogger("bot.log")


def send_email_notification(subject, message, user_info={}):

    # same email for test purposes
    sender = smtp_username
    recipient = ""

    message_full = f"Результаты викторины: {message}\n\nДанные пользователя:\nid: {user_info['id_']}\nFirst name: {user_info['first_name']}\nUsername: {user_info['username']}\nLast name: {user_info['last_name']}\nLanguage: {user_info['language_code']}"
    msg = MIMEText(message_full)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    print("trying to connect to smtp server")
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
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


def send_email_feedback(subject, message):

    sender = smtp_username
    recipient = ""

    body = message
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    print("trying to connect to smtp server")
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            print("server context")
            server.login(smtp_username, smtp_password)
            print("logged in")
            server.sendmail(sender, recipient, msg.as_string())
            print("sent")
    except Exception as e:
        print(e)
        logger.log(
            "error",
            f"Error occured when trying to send feedback email notification: {e}",
        )
