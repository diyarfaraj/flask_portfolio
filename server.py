from flask import Flask, render_template, url_for, request
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# contact
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return render_template('thankyou.html')
    else:
        return 'something went wrong'


def write_to_file(data):
    with open('db.csv', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
