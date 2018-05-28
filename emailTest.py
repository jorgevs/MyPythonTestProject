import smtplib

sender = 'jorge.vs@tecnohobby.net'
receivers = ['jorge.vs@tecnohobby.net']

message = """From: JorgeVS <jorge.vs@tecnohobby.net>
To: JorgeVS <jorge.vs@tecnohobby.net>
Subject: Python email test
Content-type: text/html
MIME-Version: 1.0

This is a test e-mail message."""

try:
    #mailserver = smtplib.SMTP('mail.tecnohobby.net', 25)
    mailserver = smtplib.SMTP_SSL('e19.ehosts.com', 465)
    mailserver.login("jorge.vs@tecnohobby.net", "XXXXXXX")
    mailserver.sendmail(sender, receivers, message)
    print("Successfully sent email")
except SMTPException:
    print("Successfully sent email")
