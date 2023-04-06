from flask import Flask, render_template, request, redirect, url_for
from database import DB

app = Flask(__name__)
datab = DB()

@app.route("/")
def home():
    return render_template("studentForm.html")

@app.route("/display")
def display():
    return "<h1>Display info</h1>"

@app.route("/students")
def append_student():
    students = datab.run_query("SELECT * FROM students")
    return render_template("studentList.html", students = students)

@app.route("/", methods=['POST'])
def add_student():
    firstName = request.form.get("firstName")
    lastName = request.form.get("lastName")
    phone = request.form.get("phone")
    dob = request.form.get("dob")
    rollNo = request.form.get("rollNo")
    email = request.form.get("email")
    address = request.form.get("address")


    print(firstName, lastName, phone, dob, rollNo, email, address)
    conn = datab.connection()
    c = conn.cursor()
    c.execute(f"INSERT INTO students(firstName, lastName, contactNumber, rollNo, email, dob, address) VALUES('{firstName}', '{lastName}', {phone}, {rollNo}, '{email}', '{dob}', '{address}')")
    conn.commit()
    conn.close() 

    return redirect(url_for('append_student'))
    

if __name__ == '__main__':
    app.run(host= "0.0.0.0", debug=True)