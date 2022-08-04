from flask import Flask, render_template, url_for, request, redirect
import csv


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

def write_to_file(data):
	with open('database.txt', mode='a') as database :
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'{email},\n{subject},\n{message}\n\n')


def write_to_CSV(data):
	with open('database.csv', newline='', mode='a') as database2 :
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	try :
    		data=request.form.to_dict()
    		write_to_file(data)
    		write_to_CSV(data)
    	except :
    		return 'did not save to database'
    	return redirect('/thankyou.html')
    else : 
    	return 'something wrong'