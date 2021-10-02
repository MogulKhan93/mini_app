import smtplib
from email.mime.text import MIMEText


def send_email(message):
    sender = 'compapk@gmail.com'  # Enter the sender's email here
    password = 'pk159753pc'  # Enter the sender's email password here
    recipient = 'mogulkahn329@gmail.com'  # Enter the recipient's email here

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, recipient, f'Subject: CHECK THIS OUT!\n{message}')

        # msg = MIMEText(message)  # Required to work with Cyrillic
        # msg['Subject'] = 'This is the subject of the message'
        # server.sendmail(sender, recipient, msg.as_string())

        return 'The message was sent successfully'
    except Exception as _ex:
        return f'{_ex}\nCheck your login or password please!'


def main():
    message = input('Type your message: ')
    print(send_email(message=message))


if __name__ == '__main__':
    main()
