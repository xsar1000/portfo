from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def root_folder():
    return render_template('index.html')


# @app.route('/index.html')
# def home_folder():
#     return render_template('index.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/work.html')
# def work():
#     return render_template('work.html')


# @app.route('/about.html')
# def about():
#     return render_template('about.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# copying and pasting the app.routes is not efficient. so use the below to make it dynamically generated
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# submit contact form and save the information
# data submitted can be captured and used in py code
# data in the form can be accessed using request.form[] -> request module needs to be imported
# the form data can be grabbed individually using request.form['input_name']
# all form data can be grabbed in a dictionary using request.form.to_dict()
# after data is submitted, redirect() to the thank you page.
# redirect() needs redirect module to be imported
# names can be added on the thank you page with the {{}}
# create a function to open/write to the database

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


# import csv and write to it
def write_to_csv(data):
    with open('database.csv', mode='a') as database_csv:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            database_csv,  delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        return redirect('contact_thanks.html')
    else:
        return 'form submission failed!'

# deploying the app to python anywhere
#   - create project on gh
#   - clone proj into local folder
#   - copy important files into local proj folder
@app.route('/admin')
def admin():
    s = 1 + 2
    return s
