from flask import Flask, render_template, url_for, request, redirect
import csv
import smtplib
from email.message import EmailMessage
from string import Template
# from pasthlib import Path

app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/work.html')
# def work():
#     return render_template('work.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# #@app.route('/user')

# # @app.route("/favicon.ico")
# # def blog():
# #     return 

# def write_to_file(data):
# 	with open('database.txt', mode='a') as database :
# 		email = data["email"]
# 		subject = data["subject"]
# 		message = data["message"]
# 		file = database.write(f'{email},\n{subject},\n{message}\n\n')
# def send_email(data):
#     email = data["email"]
#     subject = data["subject"]
#     message = data["message"]
def send_email1(data):
    me = 'richiekazu@gmail.com'
    password = 'teezkcylpsoiettm'
    #server = 'smtp.gmail.com:587
    # =============================================================================
    # SET THE INFO ABOUT THE SAID EMAIL
    # =============================================================================

    sent_to = 'richiekazu@gmail.com'
    sent_subject = data["subject"]
    who=data["email"]
    mess=data["message"]
    sent_body = (f"from {who},\n{mess} \n")


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

    # me = 'richiekazu@gmail.com'
    # password = 'teezkcylpsoiettm'
    
    # text = text.format(table=tabulate(data, headers="firstrow", tablefmt="grid"))
    # print(text)
    # mess1 = text.format(table=tabulate(data, headers="firstrow", tablefmt="grid"))
    # print(mess1)
    # html = html.format(table=tabulate(data, headers="firstrow", tablefmt="html"))
    # print(html)
    # message = MIMEMultipart( "alternative", None, [MIMEText(text), MIMEText(html,'html'), MIMEText(mess1)])
    # message['Subject'] = subject
    # message['From'] = me
    # message['To'] = you
    # server = smtplib.SMTP(server)
    # server.ehlo()
    # server.starttls()
    # server.login(me, password)
    # server.sendmail(me, you, message.as_string())
    # server.quit()

def write_to_CSV(data):
	with open('database.csv', newline='', mode='a') as database :
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])
    
    # with open('database.csv',  mode='r') as database1 :
    #     email = data["email"]
    #     subject = data["subject"]
    #     message = data["message"]
        # csv_writer = csv.writer(database1,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        # csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try :
            data=request.form.to_dict()
            # write_to_file(data)
            write_to_CSV(data)
            send_email1(data)
        except :
            return 'did not save to database'
        return redirect('/thankyou.html')
    else :
        return 'something wrong'



