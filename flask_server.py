from flask import Flask,render_template,request,redirect
import csv

app = Flask(__name__)


@app.route("/")
def about():
    return render_template("index.html")

@app.route("/<string:html_page>")
def index(html_page):
    return render_template(html_page)

def write_to_csv(data):
    
    with open('db.csv',newline='',mode='a') as csv_file:

        csvfile = csv.writer(csv_file,delimiter=",")
        email = data['email']
        subject = data['subject']
        msg = data['msg']
        csvfile.writerow([email,subject,msg])

def write_to_file(data):
    
    with open('database.txt',mode='a') as db:

        
        email = data['email']
        subject = data['subject']
        msg = data['msg']

        file=db.write(f"\n{email},{subject},{msg}")

        
    

@app.route("/submit",methods=['POST','GET'])
def submit():
    if request.method =='POST':
        data = request.form.to_dict()
        print(data)
        write_to_csv(data)

    return redirect('/thanku.html')

# @app.route("/about.html")
# def about():
#     return render_template("about.html")

# @app.route("/components.html")
# def components():
#     return render_template("components.html")

# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")

# @app.route("/work.html")
# def work():
#     return render_template("work.html")

# @app.route("/works.html")
# def works():
#     return render_template("works.html")


