import smtplib
from email.message import EmailMessage
from string import Template
from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

data = {
    'email' : 'michaelrichierr7@gmail.com',
    'subject' : 'test',
    'message' : 'hello'
}

# def send_email(data):
#     text = """
#     Hello Richie,

#     u GOt a message

#     {table}

#     Regards,

#     Arun"""

#     html = """
#     <html>
#     <body>
#         <p>Hello Richie</p>
#         <p>u got an offer</p>
#         {table}
#         <p>Regards,</p>
#         <p>Arun</p>
#     </body>
#     </html>
#     """

#     me = 'richiekazu@gmail.com'
#     password = 'teezkcylpsoiettm'
#     server = 'smtp.gmail.com:587'
#     you = data["email"]
#     subject = data["subject"]
#     mess = data["message"]

#     text = text.format(table=tabulate(data, headers="firstrow", tablefmt="grid"))
#     print(text)
#     mess1 = text.format(table=tabulate(data, headers="firstrow", tablefmt="grid"))
#     print(mess1)
#     html = html.format(table=tabulate(data, headers="firstrow", tablefmt="html"))
#     print(html)

#     message = MIMEMultipart( "alternative", None, [MIMEText(text), MIMEText(html,'html'), MIMEText(mess1)])
#     message['Subject'] = subject
#     message['From'] = me
#     message['To'] = you
    
#     server = smtplib.SMTP(server)
#     server.ehlo()
#     server.starttls()
#     server.login(me, password)
#     server.sendmail(me, you, message.as_string())
#     server.quit()


# send_email(data)
def send_email1(data):
    me = 'richiekazu@gmail.com'
    password = 'teezkcylpsoiettm'
    #server = 'smtp.gmail.com:587'
    you = 'michaelrichierr7gmail.com'
    froms= data["email"]

    # =============================================================================
    # SET THE INFO ABOUT THE SAID EMAIL
    # =============================================================================

    sent_to = 'richiekazu@gmail.com'
    sent_subject = data["subject"]
    sent_body = data["message"]

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (me, ", ".join(sent_to), sent_subject, sent_body)

    # =============================================================================
    # SEND EMAIL OR DIE TRYING!!!
    # Details: http://www.samlogic.net/articles/smtp-commands-reference.htm
    # =============================================================================

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        
        server.login(me, password)
        server.sendmail(me, sent_to, email_text)
        server.close()

        print('Email sent!')
    except Exception as exception:
        print("Error: %s!\n\n" % exception)


send_email1(data)