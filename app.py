from flask import Flask, redirect, url_for, render_template, request, g, session
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import os

# initialization of flask
app = Flask(__name__)

# for using flak-session
app.secret_key = os.urandom(24)

# adding encryption key
app.secret_key = os.urandom(24)

# comfiguring database values
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "newuser"
app.config["MYSQL_PASSWORD"] = "Ninad2452"
app.config["MYSQL_DB"] = "ehrsystem"

# initializing database as db
db = MySQL(app)

# Home page/first page to load
@app.route("/")
def index():
    return render_template("index.html")


# about-us
@app.route("/about_us")
def about_us():
    return render_template("about_us.html")


# products and services
@app.route("/product")
def product():
    return render_template("product.html")


# contact
@app.route("/contact")
def contact():
    return render_template("contact.html")


# help
@app.route("/help")
def help():
    return render_template("help.html")


# registration
@app.route("/registration")
def registration():
    return render_template("registration.html")


# login page
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.pop("user", None)
        uid = request.form["userid"]
        pswd = request.form["pass"]
        table = request.form["table"]
        cur = db.connection.cursor()
        query = f"select * from login_{table} where user_id={uid}"
        cur.execute(query)
        usernamess = cur.fetchall()
        try:
            if usernamess[0][1] == pswd:
                session["user"] = request.form["userid"]
                return redirect(url_for("redirecting", table=table))
            else:
                return "password incorrect"
        except:
            return "invalid username"
    return render_template("login.html")


# redirecting after logging in
@app.route("/redirecting/<table>")
def redirecting(table):
    if table == "patient":
        return redirect("/patient_home")
    elif table == "doctor":
        return redirect("/doctor_home")
    elif table == "receptionist":
        return redirect("/patient_home.html")
    elif table == "pathologist":
        return redirect("/patient_home.html")
    else:
        return "please login"


# checking and initialising user
@app.before_request
def before_request():
    g.user = None

    if "user" in session:
        g.user = session["user"]


# logout
@app.route("/logout")
def logout():
    if g.user:
        session.pop("user", None)
        return redirect(url_for("login"))
    return "you are already logged out"


# -------------------------------------------------------------------------------------------------------------------------

# patient

# patient home page
@app.route("/patient_home")
def patient_home():
    if g.user:
        curser = db.connection.cursor()
        query = f"select * from patient where p_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("patient_home.html", userinfo=userdetail)
    return "please login first"


# patient  profile page
@app.route("/patient_profile")
def patient_profile():
    if g.user:
        curser = db.connection.cursor()
        query = f"select * from patient where p_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("patient_profile.html", userinfo=userdetail)
    return "please login first"


# patient session
@app.route("/patient_session")
def patient_session():
    if g.user:
        curser = db.connection.cursor()
        query = f"select * from patient where p_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("patient_session.html", userinfo=userdetail)
    return "please login first"


# patient appointments
@app.route("/patient_apts")
def patient_apts():
    if g.user:
        curser = db.connection.cursor()
        query = f"select * from patient where p_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("patient_apts.html", userinfo=userdetail)
    return "please login first"


# patient diet
@app.route("/patient_diet")
def patient_diet():
    if g.user:
        curser = db.connection.cursor()
        query = f"select * from patient where p_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("patient_diet.html", userinfo=userdetail)
    return "please login first"


# patient prescription
@app.route("/patient_prescription")
def patient_prescription():
    if g.user:
        curser = db.connection.cursor()
        query = f"select * from patient where p_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("patient_prescription.html", userinfo=userdetail)
    return "please login first"


# patient reports
@app.route("/patient_reports")
def patient_reports():
    if g.user:
        curser = db.connection.cursor()
        query = f"select * from patient where p_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("patient_reports.html", userinfo=userdetail)
    return "please login first"


# -------------------------------------------------------------------------------------------------------------------------

# Doctor

# Doctor's home
@app.route("/doctor_home")
def doctor_home():
    if g.user:
        curser = db.connection.cursor()
        query = f"select * from doctor where dr_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("doctor_home.html", userinfo=userdetail)
    return "please login first"


# Doctor add patient
@app.route("/doctor_addPatient", methods=["POST", "GET"])
def doctor_addPatient():
    if g.user:
        if request.method == "POST":
            pat_id = request.form["pid"]
            prob = request.form["prob"]
            print(pat_id, prob)
            return "successfully added patient"
        else:
            curser = db.connection.cursor()
            query = f"select * from doctor where dr_id={g.user}"
            result = curser.execute(query)
            userdetail = curser.fetchall()
            return render_template("doctor_addPatient.html", userinfo=userdetail)
    return "please login first"


# doctor sessions
@app.route("/doctor_session")
def doctor_session():
    if g.user:
        curser = db.connection.cursor()
        query = f"select distinct p.p_fname,p.p_lname,p.p_phone,s.ses_num from patient p, session s,doctor d where p.p_id=s.p_id and s.dr_id=d.dr_id and d.dr_id={g.user}"
        result = curser.execute(query)
        output = curser.fetchall()
        return render_template("doctor_session.html", sess=output)
    return "please login first"


# Doctor's patlust
@app.route("/doctor_patlust")
def doctor_patlust():
    if g.user:
        curser = db.connection.cursor()
        query = f"select * from doctor where dr_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("doctor_patlust.html", userinfo=userdetail)
    return "please login first"


# -------------------------------------------------------------------------------------------------------------------------

# to run and debug
if __name__ == "__main__":
    app.run(debug=True)