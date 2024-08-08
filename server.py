
from flask import Flask,render_template,request,redirect,url_for
from jinja2 import Environment, FileSystemLoader
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/pricing.html")
def pricing():
    return render_template('./pricing.html')

@app.route("/components.html")
def components():
    return render_template('./components')

@app.route("/contact.html")
def aboutw():
    return render_template('./contact.html')

def write_to_csv(data):
    with open('database.csv',mode= 'a') as database2:
        email=request.data["email"]
        subject=request.data["subject"]
        message=request.data["message"]
        csv=csv.writer(database2,delimiter=',',quotechar='"',newline="",quoting=csv.QUOTE_MINIMAL)
        csv.writer.writerow([email,message,subject])



@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method=='POST':
        try:
            data=request.form.to_dict()
            write_to_csv(data)
            return 'horrray!!'
        except:
            return "error"
    else:
        return 'something went wrong!'






if __name__ == '__main__':
    app.run(debug=True)


